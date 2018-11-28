#!/usr/bin/env python2.6
from __future__ import absolute_import, division, print_function

known = [
    ("y qee", "a zoo"),
    ("ejp mysljylc kd kxveddknmc re jsicpdrysi",
     "our language is impossible to understand"),
    ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
     "there are twenty six factorial possibilities"),
    ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
     "so it is okay if you want to just give up"),
    ("z", "q") # Only missing character
]

def build_translation():
    translation = dict()
    for googlerese, english in known:
        for g, e in zip(googlerese, english):
            translation[g] = e
    return translation

def translate(googlerese, translation=build_translation()):
    return ''.join(translation[g] for g in googlerese)

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        print("Case #%d:" % i, translate(raw_input()))
    #for googlerese, english in known:
    #    t = translate(googlerese)
    #    print(googlerese, "=>", t, t==english)
    #print(''.join(sorted(translate(" abcdefghijklmnopqrstuvwxyz"))))
