"""Unit tests for type-directed-mock-synthesizer."""
import unittest
from dataclasses import dataclass
from typing import List, Optional
from type_directed_mock_synthesizer.synthesizer import MockSynthesizer


@dataclass
class SampleConfig:
    retries: int
    endpoint: str
    tags: List[str]


class TestMockSynthesizer(unittest.TestCase):
    def setUp(self):
        self.syn = MockSynthesizer()

    def test_synthesize_primitives(self):
        self.assertIsInstance(self.syn.synthesize(int), int)
        self.assertIsInstance(self.syn.synthesize(str), str)

    def test_synthesize_dataclass(self):
        obj = self.syn.synthesize(SampleConfig)
        self.assertIsInstance(obj, SampleConfig)
        self.assertIsInstance(obj.retries, int)
        self.assertIsInstance(obj.tags, list)
