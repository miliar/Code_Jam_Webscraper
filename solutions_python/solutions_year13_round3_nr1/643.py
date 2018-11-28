import sys
from functools import reduce
import operator
import numpy as np

input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip(".py"), 'w')

input_size = int(input_file.readline().rstrip("\n"))

vowels = ('a', 'e', 'i', 'o', 'u')
case = 1

for i in range(input_size):
    (name, n) = input_file.readline().rstrip("\n").split(" ")
    n = int(n)
    name = list(name)

    l = 0
    conson = []
    result = 0
    for letter in name:
        if letter not in vowels:
            conson.append(l)
        l = l + 1
    subs =[]
    for j in range(len(conson)):
        # print(conson[j: j +n], list(range(conson[j], conson[j] + n )))
        # print(conson[j:j + n] == list(range(conson[j], conson[j] + n)))
        # print(len(conson[j:n]))
        if len(conson[j:j + n]) < n:
            break
        if (conson[j: j + n] == list(range(conson[j], conson[j] + n))):
            subs.append((conson[j],conson[j + n - 1]))
#    print(subs)
    subsDone = []
    for string in subs:
        for k in range(len(name[:string[0]]) + 1):
            notContinue = False
            for prec in subs[:subs.index(string)]:
                if (string[0] - k <= prec[0]):
                    notContinue = True
            if notContinue:
                break
            for l in range(len(name[string[1] + 1:]) + 1):
#                print(name[string[0] -k:string[1] + l  +1])
                result += 1
#print(len(name[:string[0]]), len(name[string[1] + 1:]))
        #result += (1 + len(name[:string[0]])) * (len(name[string[1] + 1:]) + 1)
    print(result)
    output_file.write("Case #" + str(case) + ': ' + str(result) + '\n')
    case += 1









