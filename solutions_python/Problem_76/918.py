#!/usr/bin/python
#Bot Trust - Andrey Polyakov
import itertools

def main():
    f = open("file.in", "r")
    lines = f.readlines()
    f.close()
    cases = int(lines[0])
    curr_case = 1
    for xx in range(cases):
        li = lines[curr_case*2].split()
        sean_max = 0    
        for x in range(len(li))[1:]:    
            tu2 = tuple(itertools.combinations(li,x))
            li3 = []
            for y in range(len(tu2)):
                li2 = li[:] # create a copy            
                for i in range(x):
                    del(li2[li2.index(tu2[y][i])])
                li3.append(li2)
            # all combinations of sets        
            one = li3
            two = tu2
            for i in range(len(one)):
                xor_val1 = 0
                xor_val2 = 0            
                for j in range(len(one[i])):
                    xor_val1 = xor_val1 ^ int(one[i][j])
                for j in range(len(two[i])):
                    xor_val2 = xor_val2 ^ int(two[i][j])
                if xor_val1 == xor_val2:
                    sum1 = 0
                    sum2 = 0
                    for j in range(len(one[i])):
                        sum1 += int(one[i][j])
                    for j in range(len(two[i])):
                        sum2 += int(two[i][j])
                    if sum1 > sum2:
                        if sum1 > sean_max:
                            sean_max = sum1
                    else:
                        if sum2 > sean_max:
                            sean_max = sum2
        if sean_max == 0:
            print "Case #" + str(curr_case) + ": NO"
        else:
            print "Case #" + str(curr_case) + ": " + str(sean_max)
        curr_case += 1
        sean_max = 0

if __name__ == "__main__":
    main()
