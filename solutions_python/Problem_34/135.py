# Marius Damarackas (m.damarackas@gmail.com)
# Google CodeJam, Qualification Round 2009, Alien Language

import re

def possible_words(dictionary, pattern):
    re_pattern = "^" + pattern.replace("(", "[").replace(")", "]") + "$"
    prog = re.compile(re_pattern)
    return sum(1 for word in dictionary if prog.match(word))

def main():
    file = open("input.in")
    length, words, tests = [int(x) for x in file.readline().split()]
    dictionary = [file.readline().strip() for i in range(words)]
    for case in range(1, tests + 1):
        pat = file.readline().strip()
        print("Case #", case, ": ", possible_words(dictionary, pat), sep="")

if __name__ == "__main__":
    main()
