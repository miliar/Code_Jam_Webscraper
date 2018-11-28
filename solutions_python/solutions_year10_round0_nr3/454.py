#!/usr/env/bin/python
from sys import argv

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
    (R, k, N) = map(int, input_file.readline()[:-1].split(" "))
    queue = map(int, input_file.readline()[:-1].split(" "))
    
    res = 0
    while R > 0:
        R -= 1
        ride = []
        k1 = k
        while len(queue) and k1 >= queue[0]:
            k1 -= queue[0]
            ride.append(queue.pop(0))
        res += k - k1
        queue += ride
    
    res = 'Case #' + str(i) + ': ' + str(res)
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
