#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def expectations(typednum, passlen, probs):
    # backspace
    p_correct = 1
    for backspace_count in xrange(typednum, -1, -1):
        last_pressed_idx = typednum - backspace_count - 1
        if last_pressed_idx >= 0:
            p_correct *= probs[last_pressed_idx]
        cur_len = typednum - backspace_count

        exp = (passlen - cur_len + 1 + backspace_count) + (1 - p_correct) * (passlen + 1)
        yield exp

    # hitenter
    if typednum != passlen:
        # otherwise <==> 0 backspace
        yield 2 + passlen

def main():
    numcases = int(sys.stdin.readline())

    for i in xrange(numcases):
        typednum, passlen = map(int, sys.stdin.readline().strip().split())
        probs = map(float, sys.stdin.readline().strip().split())
        print "Case #{case}: {answer}".format(case=i+1, answer=min(expectations(typednum, passlen, probs)))

if __name__ == '__main__':
    main()
