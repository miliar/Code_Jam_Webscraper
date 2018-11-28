#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import itertools

T = int(input())

for caseNo in range(T):
    ans = 0
    (Smax, Ss) = input().split(" ")
    Smax = int(Smax)
    S = list(map(int, list(Ss)))
    
    stand = 0
    for i, s in enumerate(S):
        if(i == 0):
            stand = s
        else:
            if(stand + ans >= i):
                pass
            else:
                ans = i - stand
            stand += s

    print("Case #" + str(caseNo + 1) + ": " + str(ans))
