# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:14:30 2017

@author: Trevor
"""

def bathrooms(N,K):
    remaining = K
    gaps = {N:1}
    while remaining > gaps[max(gaps)]:
        gap = max(gaps)
        num_gaps = gaps[gap]
        remaining = remaining - num_gaps
        del gaps[gap]
        (l,r) = answer(gap)
        if l in gaps:
            gaps[l] = gaps[l] + num_gaps
        else:
            gaps[l] = num_gaps
        if r in gaps:
            gaps[r] = gaps[r] + num_gaps
        else:
            gaps[r] = num_gaps
    return answer(max(gaps))
    
def answer(N):
    return((N/2,(N-1)/2))

def run(filename):
    f = open(filename,"r")
    data = f.read()
    f.close()
    inputs = data.splitlines()[1:]
    count = 1
    answer = ""
    for line in inputs:
        params = line.split(" ")
        (max_ans,min_ans) = bathrooms(int(params[0]),int(params[1]))
        print_answer = str(max_ans) + " " + str(min_ans)
        answer = answer + "Case #" + str(count)+": " + print_answer + "\n"
        count = count + 1
    f = open("OutputC","w")
    f.write(answer)
    f.close()