'''
Created on 2012/04/14

@author: hanaue51
'''
import os
os.chdir("../../../data/2012/qualification/")
filename = "B-large"
postfix_in = ".in"
postfix_out = ".out"
format = "Case #%d: %d\n"
min_score = 0
max_score = 10

infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

n_cases = int(lines[0].strip())
results = []
for i in xrange(1, len(lines)):
    elems = lines[i].strip().split()
    n_googlers = int(elems[0])
    n_surprising = int(elems[1])
    threshold = int(elems[2])
    scores = [int(elems[j]) for j in xrange(3, len(elems))]
    scores.sort()
    scores.reverse()
    answer = 0
    for j in xrange(len(scores)):
        avg = scores[j] / 3
        mod = scores[j] % 3
        if avg >= threshold:
            answer += 1
        else:
            if mod == 2:
                if threshold <= (avg + 1) and (avg + 1) <= max_score:
                    answer += 1
                elif threshold <= (avg + 2) and (avg + 2) <= max_score:
                    if n_surprising > 0:
                        answer += 1
                        n_surprising -= 1
            elif mod == 1:
                if threshold <= (avg + 1) and (avg + 1) <= max_score:
                    answer += 1
            else:
                if threshold <= (avg + 1) and (avg + 1) <= max_score and min_score <= (avg - 1):
                    if n_surprising > 0:
                        answer += 1
                        n_surprising -= 1
    results.append(format % (i, answer))

#print results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
