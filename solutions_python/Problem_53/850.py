#!/usr/bin/env python

def main():
    T = int(raw_input())

    for i in range(T):
        N, K = map(int, raw_input().split())
        print "Case #%d: %s" % (i + 1, ["OFF", "ON"][int(K & ((1<<N)-1)) == (1<<N)-1])

if __name__ == '__main__':
    main()
