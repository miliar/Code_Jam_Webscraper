#!/usr/bin/env python
#coding:utf-8


def translate(text):
    mapping =  {' ': ' ',
            'a': 'y',
            'b': 'h',
            'c': 'e',
            'd': 's',
            'e': 'o',
            'f': 'c',
            'g': 'v',
            'h': 'x',
            'i': 'd',
            'j': 'u',
            'k': 'i',
            'l': 'g',
            'm': 'l',
            'n': 'b',
            'o': 'k',
            'p': 'r',
            'q': 'z',
            'r': 't',
            's': 'n',
            't': 'w',
            'u': 'j',
            'v': 'p',
            'w': 'f',
            'x': 'm',
            'y': 'a',
            'z': 'q'}
    return_str = ""
    for t in text:
        return_str = return_str + mapping[t]

    return return_str

def main():
    num_of_cases = int(input())
    for i in range(num_of_cases):
        text = input().strip()
        print("Case #%d: %s"%(i+1,translate(text)))

if __name__ == "__main__":
    main()
