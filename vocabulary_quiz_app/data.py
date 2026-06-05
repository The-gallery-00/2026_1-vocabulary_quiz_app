from __future__ import annotations

from vocabulary_quiz_app.quiz_logic import Word

WORDS: list[Word] = [
    Word(term="apple", meaning="사과", accepted_meanings=("능금",)),
    Word(term="book", meaning="책"),
    Word(term="chair", meaning="의자", accepted_meanings=("좌석",)),
    Word(term="door", meaning="문"),
    Word(term="flower", meaning="꽃"),
    Word(term="friend", meaning="친구"),
    Word(term="music", meaning="음악"),
    Word(term="school", meaning="학교"),
    Word(term="summer", meaning="여름", accepted_meanings=("하계",)),
    Word(term="water", meaning="물"),
]
