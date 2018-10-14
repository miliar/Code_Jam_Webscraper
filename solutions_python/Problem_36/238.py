#!/usr/bin/python

cache = {}
def num_phrases(s, phrase):
    if s == phrase:
        return 1
    if len(phrase) == 0:
        return 1
    if len(s) == 0:
        return 0
    key = s, phrase
    try:
        return cache[key]
    except KeyError:
        pass
    total = 0
    if s[0] == phrase[0]:
        total += num_phrases(s[1:], phrase[1:])
        total %= 1000
    total += num_phrases(s[1:], phrase)
    total %= 1000
    cache[key] = total
    return total

def main():
    n = int(raw_input())
    for i in range(1, n+1):
        s = raw_input().strip()
        sol = num_phrases(s, "welcome to code jam")
        print "Case #%d: %04d" % (i, sol)

if __name__ == "__main__":
    main()
