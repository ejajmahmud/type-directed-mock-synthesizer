"""CLI for type-directed-mock-synthesizer."""
import sys
import argparse
from dataclasses import dataclass
from typing import List, Optional
from .synthesizer import MockSynthesizer


@dataclass
class UserProfile:
    user_id: int
    username: str
    roles: List[str]
    bio: Optional[str]


def main():
    parser = argparse.ArgumentParser(description="Type-Directed Mock Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run mock synthesis demo")
    args = parser.parse_args()

    if args.demo:
        syn = MockSynthesizer()
        mock_user = syn.synthesize(UserProfile)
        print("Synthesized Mock UserProfile:")
        print(f"  {mock_user}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
