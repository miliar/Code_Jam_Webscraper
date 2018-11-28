#!/usr/env/bin/python
from sys import argv
import re

if len(argv) < 2:
    print("Insufficient arguments. Usage: python script.py <input file> [<output file>]")
    exit()

input_file = open(argv[1])

output_file = None
if len(argv) >= 3:
    output_file = open(argv[2], 'w')

n = int(input_file.readline())

sentence = "welcome to code jam"
letters = set(sentence)
sentence_len = len(sentence)

i = 1
while i <= n:
    (N, K) = map(int, input_file.readline()[:-1].split(" "))
    
    res = "OFF"
    if (K+1) % 2**N == 0:
        res = "ON"
    
    res = 'Case #' + str(i) + ': ' + res
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
