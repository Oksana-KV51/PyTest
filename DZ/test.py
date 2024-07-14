#функция для подсчета гласных

import pytest
from main import count_vowels

#Проверьте, что функция правильно считает гласные в строке, содержащей только гласные
def test_count_vowels_only_vowels():
    assert count_vowels('aeiou') == 5
    assert count_vowels('AEIOU') == 5

#Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
def test_count_vowels_no_vowels():
    assert count_vowels('bcdfg') == 0
    assert count_vowels('BCDFG') == 0

#Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).
def test_count_vowels_mixed_characters():
    assert count_vowels('hello world') == 3
    assert count_vowels('HELLO world') == 3
    assert count_vowels('hElLo WoRlD') == 3
    assert count_vowels('h3ll0 w0rld') == 1