"""Core Type-Directed Mock Synthesizer implementation."""
import typing
import dataclasses
from typing import Dict, List, Optional, Any, get_type_hints, get_origin, get_args


class MockSynthesizer:
    def __init__(self, seed: int = 42):
        self.seed = seed
        self._counter = 0

    def synthesize(self, target_type: Any) -> Any:
        self._counter += 1

        # Check primitives
        if target_type == int:
            return 100 + self._counter
        elif target_type == float:
            return float(self._counter) + 0.5
        elif target_type == str:
            return f"mock_str_{self._counter}"
        elif target_type == bool:
            return (self._counter % 2) == 0

        # Check Generics
        origin = get_origin(target_type)
        args = get_args(target_type)

        if origin is list or origin is List:
            item_type = args[0] if args else str
            return [self.synthesize(item_type)]
        elif origin is dict or origin is Dict:
            key_type = args[0] if args else str
            val_type = args[1] if len(args) > 1 else str
            return {self.synthesize(key_type): self.synthesize(val_type)}
        elif origin is typing.Union:
            # Handle Optional (Union[T, None]) -> return T
            non_none = [a for a in args if a is not type(None)]
            if non_none:
                return self.synthesize(non_none[0])
            return None

        # Check dataclass
        if dataclasses.is_dataclass(target_type):
            hints = get_type_hints(target_type)
            kwargs = {}
            for field_name, f_type in hints.items():
                kwargs[field_name] = self.synthesize(f_type)
            return target_type(**kwargs)

        return None
