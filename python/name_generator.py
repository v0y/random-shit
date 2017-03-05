#!/usr/bin/env python
# encoding: utf-8

from random import choice

import sys


VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
    't', 'v', 'w', 'x', 'z'
]
ALL_LETTERS = VOWELS + CONSONANTS


def gen_name(template):
    string = ''
    for t in template:
        if t == '@':
            char = choice(VOWELS)
        elif t == '#':
            char = choice(CONSONANTS)
        elif t == '*':
            char = choice(ALL_LETTERS)
        else:
            char = t

        string += char

    return string


def print_names(template, iterations=1):
    for _ in range(iterations):
        print(gen_name(template))


if __name__ == '__main__':
    """"
    Usage:
        python name_generator.py template number

    Params:
        template: name template. Example: 'x@#@*'.
            @ - vovel
            # - consonant
            * - any letter
            Any other char is taken literally. 'x' in example is letter 'x'
        iterations: number of iterations (results)
    """
    try:
        iterations_ = int(sys.argv[2])
    except IndexError:
        iterations_ = 1

    print_names(sys.argv[1], iterations_)
