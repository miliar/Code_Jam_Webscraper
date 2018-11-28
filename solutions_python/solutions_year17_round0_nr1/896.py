# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 17:53:51 2017

@author: Trevor
"""

def flips(sequence,k):
    count = 0
    reached = set()
    if done(sequence):
        return 0
    else:
        count = count + 1
        iterations = generate_flips(sequence,k,reached)
        while len(iterations) > 0:
            new_iterations = set()
            for item in iterations:
                if done(item):
                    return count
                else:
                    reached.add(item)
                    new_iterations.update(generate_flips(item,k,reached))
            iterations = new_iterations
            count = count + 1
        return -1
    
def done(sequence):
    for ele in sequence:
        if ele == '-':
            return False
    return True

def generate_flips(sequence,k,reached):
    new_iterations = set()
    for i in xrange(0,len(sequence)+1-k):
        new_string = sequence[:i] + flip(sequence[i:i+k]) + sequence[(i+k):]
        if new_string not in reached:
            new_iterations.add(new_string)
            reached.add(new_string)
    return new_iterations

def flip(string):
    new_string = ""
    for i in string:
        if i == '+':
            new_string = new_string + '-'
        else:
            new_string = new_string + '+'
    return new_string

def run():
    f = open("A-small-attempt1.in","r")
    data = f.read()
    f.close()
    inputs = data.splitlines()[1:]
    answer = ""
    count = 1
    for line in inputs:
        sequence = line.split(" ")[0]
        k = line.split(" ")[1]
        line_answer = flips(sequence,int(k))
        if line_answer == -1:
            answer = answer + "Case #" + str(count) + ": IMPOSSIBLE\n"
        else:
            answer = answer + "Case #" + str(count) + ": " + str(line_answer) + "\n"
        count = count + 1
    f = open("Output","w")
    f.write(answer)
    f.close()
    