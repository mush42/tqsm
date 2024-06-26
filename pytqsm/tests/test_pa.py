# coding: utf-8

import pytest
from pytqsm import segment

# ruff: noqa: E501
tests = [
    (
        "ਸਰੋਜਿਨੀ ਨਾਇਡੂ ਦਾ ਜਨਮ 13 ਫਰਵਰੀ 1879 ਨੂੰ ਭਾਰਤ ਦੇ ਸ਼ਹਿਰ ਹੈਦਰਾਬਾਦ ਵਿੱਚ ਹੋਇਆ ਸੀ। ਉਸ ਦੇ ਪਿਤਾ ਅਘੋਰਨਾਥ ਚੱਟੋਪਾਧਿਆਏ ਇੱਕ ਨਾਮੀ ਵਿਦਵਾਨ ਅਤੇ ਮਾਂ ਬਰਾਦਾ ਸੁੰਦਰੀ ਦੇਬੀ ਕਵਿਤਰੀ ਸੀ ਅਤੇ ਬੰਗਾਲੀ ਵਿੱਚ ਲਿਖਦੀ ਸੀ।",
        [
            "ਸਰੋਜਿਨੀ ਨਾਇਡੂ ਦਾ ਜਨਮ 13 ਫਰਵਰੀ 1879 ਨੂੰ ਭਾਰਤ ਦੇ ਸ਼ਹਿਰ ਹੈਦਰਾਬਾਦ ਵਿੱਚ ਹੋਇਆ ਸੀ।",
            "ਉਸ ਦੇ ਪਿਤਾ ਅਘੋਰਨਾਥ ਚੱਟੋਪਾਧਿਆਏ ਇੱਕ ਨਾਮੀ ਵਿਦਵਾਨ ਅਤੇ ਮਾਂ ਬਰਾਦਾ ਸੁੰਦਰੀ ਦੇਬੀ ਕਵਿਤਰੀ ਸੀ ਅਤੇ ਬੰਗਾਲੀ ਵਿੱਚ ਲਿਖਦੀ ਸੀ।",
        ],
    )
]


@pytest.mark.parametrize("text,expected_sents", tests)
def test_segment(text, expected_sents):
    assert list(segment("pa", text)) == expected_sents
