#!/usr/bin/env python
import sys

def build_translation(samples):
    result = {'q' : 'z', 'z' : 'q'}
    for sample in samples:
        (encoded, plain) = sample
        for i, char in enumerate(encoded):
            result[char] = plain[i]
    return result

def translate(s, translation):
    result = ""
    for c in s:
        result += translation[c]
    return result

def main():
    samples = [["ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"],
               ["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"],
               ["de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"]]
    translation = build_translation(samples)
    for i, line in enumerate(sys.stdin):
        if line.strip():
            print "Case #{0}: ".format(i + 1) + translate(line.strip(), translation)

if __name__ == "__main__": main()
