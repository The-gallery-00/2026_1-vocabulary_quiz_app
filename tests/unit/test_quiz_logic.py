import random

from collections.abc import Sequence
from typing import TypeVar

from vocabulary_quiz_app.quiz_logic import Word, check_answer, draw_word, format_meanings

T = TypeVar("T")


def test_check_answer_normalized() -> None:
    word = Word(term="apple", meaning="사과")
    assert check_answer(word, "사과")
    assert check_answer(word, "  사과 ")
    assert not check_answer(word, "apple")


def test_check_answer_accepts_additional_meanings() -> None:
    word = Word(term="chair", meaning="의자", accepted_meanings=("좌석", "자리"))

    assert check_answer(word, "좌석")
    assert check_answer(word, " 자리 ")
    assert not check_answer(word, "책상")


def test_format_meanings_includes_primary_and_additional_meanings() -> None:
    word = Word(term="summer", meaning="여름", accepted_meanings=("하계",))

    assert format_meanings(word) == "여름, 하계"


def test_draw_word_uses_rng_choice() -> None:
    words = [Word(term="a", meaning="A"), Word(term="b", meaning="B")]

    class FixedRng:
        def choice(self, seq: Sequence[T]) -> T:
            return seq[0]

    assert draw_word(words, FixedRng()) == words[0]


def test_draw_word_empty_list_raises() -> None:
    try:
        draw_word([], random.Random())
    except ValueError as exc:
        assert "empty" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty word list")
