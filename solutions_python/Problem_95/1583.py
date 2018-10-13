#!/usr/bin/env python
# coding=utf-8

# Last modified: <2012-04-14 11:21:34 Saturday by richard>

# @version 0.1
# @author : Richard Wong
# Email: chao787@gmail.com
import sys

_input = """
y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
    """
_output = """
a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
    """

word_dict = dict()
# Rectify word_dict
word_dict["z"] = "q"

def main(lines):
    """
    linenum
    line1
    ...
    """
    learn(_input, _output)

    assert len(word_dict) > 27

    line_list = lines.split("\n")
    lineno = int(line_list[0])
    result = str()
    for i in range(1, lineno + 1):
        result += "Case #%d: %s\n" % (i, translate(line_list[i]))
    print result,
    return

def translate(words):
    global word_dict
    result = str()
    for ch in words:
        assert ch in word_dict
        result += word_dict[ch]

    return result

def learn(in_text, out_text):
    in_len = len(in_text)
    out_len = len(out_text)
    assert in_len == out_len
    global word_dict
    for i in range(in_len):
        if in_text[i] in word_dict:
            assert word_dict[in_text[i]] == out_text[i]
        else:
            word_dict[in_text[i]] = out_text[i]
    return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print u"""You can append a filename or input text.\n"""
    elif len(sys.argv) > 3:
        print u"""Only one file accepted..\n"""
    else:
        filename = sys.argv[1]
        with open(filename, "r") as f:
            main(f.read())



