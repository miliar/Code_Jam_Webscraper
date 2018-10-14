#!/usr/bin/python

def main():
    d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

    n = int(raw_input())
    tt = 1

    for i in xrange(n):
        m = raw_input()
        print ("Case #%d: %s" % (tt, "".join(map(lambda x: d[x], m))))
        tt += 1

if __name__ == "__main__":
    main()
