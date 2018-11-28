#!/usr/bin/python

import sys
import fileinput

debug=True
debug=False

def dprint(s):
    if debug:
        print(s)
def simplify(string):
    #dprint("--simplify: %s"%string)
    last=string[0]
    result=[last]
    for i in range(len(string)):
        if string[i] != last:
            result.append(string[i])
        last=string[i]
    #dprint("--simplify result: %s"%result)
    return result
def find_occurrences(string):
    last_pos=0
    last_char=string[last_pos]
    count=0
    result=[]
    for i in range(len(string)):
        char=string[i]
        if char == last_char:
            count+=1
        else:
            result.append(count)
            last_char=char
            count=1
        if i == len(string)-1:
            result.append(count)
    return result

f=open(sys.argv[1])
num_line=int(f.readline().strip())
dprint("num lines: %i"%num_line)
for case_n in range(1,num_line+1):
    num_strings=int(f.readline().strip())
    strings=[]
    for i in range(num_strings):
        strings.append(list(f.readline().strip()))
    dprint("strings: %s"%strings)
    simple_string=simplify(strings[0])
    possible=True
    for i in range(num_strings):
        if simplify(strings[i]) != simple_string:
            possible=False
            continue
    if possible == False:
        print("Case #%i: Fegla Won"%case_n)
        continue
    occurrences=[]
    for i in range(num_strings):
        occurrences.append(find_occurrences(strings[i]))
    total_changes = 0
    for i in range(len(simple_string)):
        occ = []
        for j in range(len(occurrences)):
            occ.append(occurrences[j][i])
        maxim=max(occ)
        min_sum=200
        for num_char in range(1,maxim+1):
            suum=0
            for j in range(len(occ)):
                suum += abs(occ[j] - num_char)
            if suum < min_sum:
                min_sum=suum
        dprint("min change %i: %i"%(i,min_sum))
        total_changes += min_sum
    print("Case #%i: %i"%(case_n,total_changes))

    dprint("")




