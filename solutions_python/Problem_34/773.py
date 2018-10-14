# -*- coding: utf-8 -*-
siaip = open("A-large.in", "r")
ivestis = []
for line in siaip:
    ivestis.append(line.strip())
L, D, N = ivestis[0].split(" ")
word_length, word_count, case_count = int(L), int(D), int(N)

words= ivestis[1:word_count+1]
cases = ivestis[1+word_count:]
formatted=[]
start=False
for case in cases:
    case_tmp = []
    expr=[]
    for char in case:
        if char == "(":
            start=True
        elif start==True and char != ")":
            expr.append(char)
        elif char == ")":
            case_tmp.append(expr)
            expr=[]
            start=False
        else:
            case_tmp.append(char)
    formatted.append(case_tmp)
cases = formatted
for i in range(0, case_count):
    count=0
    for word in words:
        letter_no=0
        letter_count=0
        for letter in word:
            for possible_letter in cases[i][letter_no]:
                if possible_letter == letter:
                    letter_count +=1
            letter_no += 1
        if letter_count == word_length:
            count += 1
    print ("Case #%d: %d" % (i+1, count))