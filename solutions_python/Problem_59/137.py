#!/usr/bin/python


for case in range(input()):
    N, M = [int(x) for x in raw_input().split()]
    root = dict()
    for n in range(N):
        dir = raw_input()[1:].split('/')
        cur = root
        for d in dir:
            if not d in cur:
                cur[d] = dict()
            cur = cur[d]
    mkdir = 0

    for m in range(M):
        make_dir = raw_input()[1:].split('/')
        cur = root
        for d in make_dir:
            if d not in cur:
                mkdir = mkdir + 1
                cur[d] = dict()
            cur = cur[d]

    print("Case #%s: %s" % (case + 1, mkdir))

