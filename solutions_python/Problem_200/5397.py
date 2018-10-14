#!/usr/bin/env python3
# -*- coding: utf-8 -*-

T = int(input())
for i in range(1,T+1):
    N = int(input())
    last_tidy_number = 0
    tidy_number_found = 0
    while (tidy_number_found !=1):
        blup = str(N)
        tidy = 1 # a priori tidy
        for j in range(len(blup)-1):
            premier = int(blup[j])
            second = int(blup[j+1])
            if premier>second:
                tidy = 0
        if tidy:
            tidy_number_found = 1
        else:
            N =N-1
    print("Case #{}: {}".format(i,N))
