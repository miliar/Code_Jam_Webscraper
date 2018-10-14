#!/usr/local/bin/python
import numpy as np

k_max = 1000000

num_cases = int(raw_input())

for case_no in range(1, num_cases+1):
    (C, F, X) = map(float, raw_input().split(' '))
    v    = 1. / (2. + np.arange(k_max, dtype=float) * F)
    options = np.cumsum(C*v) - C*v + X*v

    print "Case #%d: %0.7f" % (case_no, np.min(options))
    pass


