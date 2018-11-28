#!/usr/bin/env python

import sys

PLAIN_FILE="./plain.txt"
ENCRYPTED_FILE="./encrypted.txt"

mapping = {'y': 'a', 'e': 'o', 'q': 'z', 'z': 'q'}

for p_line, e_line in zip(open(PLAIN_FILE), open(ENCRYPTED_FILE)):
    # p_line = p_line.rstrip()
    # e_line = e_line.rstrip()
    for p, e in zip(p_line, e_line):
        mapping[e] = p

cnt = 0
for line in sys.stdin.readlines():
    if cnt == 0:
        cnt_max = int(line)
        cnt += 1
        continue
    sys.stdout.write("Case #" + str(cnt) + ": ")
    for char in line:
        sys.stdout.write(mapping[char])
    if cnt >= cnt_max:
        break
    cnt += 1
