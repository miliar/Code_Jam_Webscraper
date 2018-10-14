from __future__ import with_statement
import string

with open("file.txt") as f:
    word_len, num_words, num_cases = f.readline().split()
    word_len = int(word_len)
    num_words = int(num_words)
    num_cases = int(num_cases)
    words = []
    cases = []
    for i in range(num_words):
        words.append(f.readline().strip())
    for i in range(num_cases):
        cases.append(f.readline().strip())

new_cases = []

for case in cases:
    new_case = []
    i = 0
    while i < len(case):
        if case[i] in string.ascii_lowercase:
            new_case.append([case[i]])
            i = i + 1
        else:
            i = i + 1
            wildcard =[]
            while case[i] is not ")":
                wildcard.append(case[i]) 
                i = i + 1
            new_case.append(wildcard)
            i = i + 1
    new_cases.append(new_case)

for i in range(num_cases):
    successes = 0
    for word in words:
        for j in range(word_len):
            success = False
            try:
                index = new_cases[i][j].index(word[j])
            except:
                break       
            success = True
        if success is True:
            successes += 1
    print ("Case #" + `i + 1` + ": " + `successes`)