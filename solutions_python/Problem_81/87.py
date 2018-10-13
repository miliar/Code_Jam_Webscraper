#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import sys

lines = sys.stdin.readlines()
i = 1
index = 0
while i < len(lines):
    index += 1
    num = int(lines[i])
    matrix = [x.strip() for x in lines[i + 1: i + num + 1]]
    i += num + 1

    # get wp.
    wp = [0] * num
    for j in range(num):
        x, y = 0, 0
        for c in matrix[j]:
            if c == "1": x += 1
            elif c == "0": y += 1
        wp[j] = (x, x + y)

    # get owp.
    owp = [0] * num
    for j in range(num):
        wps = []
        for k in range(num):
            if matrix[j][k] == ".": continue
            if matrix[j][k] == "0":
                wps.append((wp[k][0] - 1.0) / (wp[k][1] - 1.0))
            else:
                wps.append((wp[k][0]) / (wp[k][1] - 1.0))
        owp[j] = sum(wps) / len(wps)

    # get oowp.
    oowp = [0] * num
    for j in range(num):
        owps = []
        for k in range(num):
            if matrix[j][k] == ".": continue
            owps.append(owp[k])
        oowp[j] = sum(owps) / len(owps)

    # get rpi.
    rpi = [0] * num
    for j in range(num):
        rpi[j] = 0.25 * wp[j][0] / wp[j][1] + 0.50 * owp[j] + 0.25 * oowp[j]

    print "Case #%d:" % index
    for r in rpi:
        print r

