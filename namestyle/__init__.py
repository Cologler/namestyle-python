# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import re
import typing

_re_sep = re.compile('[_ ]')
_re_word = re.compile('^[a-zA-Z][a-z]+')

_re_split_words = re.compile('^([a-z][a-z]+)(?:_([a-z][a-z]+))*$')

def split_words(text: str) -> typing.List[str]:
    'split a str into a typing.List[str]'
    words = []
    for part in _re_sep.split(text):
        while True:
            match = _re_word.match(part)
            if match:
                word = match.group(0)
                words.append(word)
                part = part[len(word):]
            else:
                break
    return tuple(words)

def to_snake_case(words: typing.List[str]) -> str:
    return '_'.join(w.lower() for w in words)

def to_pascal_case(words: typing.List[str]) -> str:
    return ''.join(w[0].upper() + w[1:].lower() for w in words)

def to_camel_case(words: typing.List[str]) -> str:
    return ''.join(
        (w[0].upper() if i > 0 else w[0].lower()) + w[1:].lower() for i, w in enumerate(words))
