# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from namestyle import split_words
from namestyle import (
    to_snake_case,
    to_pascal_case,
    to_camel_case,
)

def test_single_word():
    assert split_words('Function') == ('Function', )

def test_single_word_lowercase():
    assert split_words('function') == ('function', )

def test_snake_case():
    text = 'do_whatever_you_want'
    words = split_words(text)
    assert words == ('do', 'whatever', 'you', 'want')
    assert text == to_snake_case(words)

def test_pascal_case():
    text = 'DoWhateverYouWant'
    words = split_words(text)
    assert words == ('Do', 'Whatever', 'You', 'Want')
    assert text == to_pascal_case(words)

def test_camel_case():
    text = 'doWhateverYouWant'
    words = split_words(text)
    assert words == ('do', 'Whatever', 'You', 'Want')
    assert text == to_camel_case(words)

def test_sentence():
    text = 'Do whatever you want'
    words = split_words(text)
    assert words == ('Do', 'whatever', 'you', 'want')
