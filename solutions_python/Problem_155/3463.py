#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AMiT Kumar | dtu.amit@gmail.com

if __name__ == "__main__":
    testcases = int(raw_input())

    for cases in xrange(1, testcases+1):
        Smax, aud = raw_input().split()
        Smax, aud = int(Smax), str(aud)
        aud = map(int, aud)

        friends, standing = 0, 0

        for shyval, people in enumerate(aud):
            if people != 0:
                if standing < shyval:
                    friends += shyval - standing
                    standing += (people + friends)
                else:
                    standing += people

        print("Case #%i: %i" % (cases, friends))
