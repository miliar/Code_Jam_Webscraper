#!/bin/python
input_file=open("B-large.in","r")
output_file=open("B-large.out","w")
lines=input_file.readlines()
for iline in range(0,len(lines)):
    if iline==0:
        continue
    numbers=lines[iline].split()
    print numbers
    n_dancer=int(numbers[0])
    n_surprise=int(numbers[1])
    p=int(numbers[2])
    n_count=0
    for idancer in range(0, n_dancer):
        score=int(numbers[idancer+3])
        if score>=(3*p-2):
        #    print [score, 3*p-2]
            n_count=n_count+1
        elif score!=0 and score>=(3*p-4) and n_surprise>0:
        #    print score
            n_count=n_count+1
            n_surprise=n_surprise-1
    output_file.write("Case #%d: %d\n" % (iline, n_count))
