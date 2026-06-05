from __future__ import annotations

import random

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")


class RandomChooser(Protocol):
    def choice(self, seq: Sequence[T]) -> T:
        ...


@dataclass(frozen=True)
class Word:
    term: str
    meaning: str
    accepted_meanings: tuple[str, ...] = ()

    def all_meanings(self) -> tuple[str, ...]:
        return (self.meaning, *self.accepted_meanings)


def normalize_answer(text: str) -> str:
    return " ".join(text.strip().lower().split())


def check_answer(word: Word, user_input: str) -> bool:
    normalized_input = normalize_answer(user_input)
    return any(
        normalized_input == normalize_answer(meaning)
        for meaning in word.all_meanings()
    )


def format_meanings(word: Word) -> str:
    return ", ".join(word.all_meanings())


def draw_word(words: list[Word], rng: RandomChooser | None = None) -> Word:
    if not words:
        raise ValueError("Word list is empty")
    chooser: RandomChooser = rng if rng is not None else random
    return chooser.choice(words)
