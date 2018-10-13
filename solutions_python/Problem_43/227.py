'''
Created on 2009/9/13
@author: Cody
'''
import math
filename = "sample"
filename = "A-small-attempt3"
fin = open(filename + ".in", "r")
fout = open(filename + ".out", "w")
T = int(fin.readline())

case_num = 0


for t in range(T):
    carry = [0]
    carry.extend(range(100)[2:])
    carry.reverse()
    case_num +=1
    content = fin.readline()[:-1]
    ans = []
    for c in content:
        ans.append([c,'?'])
        
    ans[0][1] = 1
    for c in ans:
        if c[0] == ans[0][0]:
            c[1] =1
    print ans
    
    index = 0
    while True:
        try:
            if ans[index][1] =='?':
                num = ans[index][0]
                mark = carry.pop()
                ans[index][1] = mark
                for  c in ans[index:]:
                    if c[0] == num:
                        c[1] = mark
        except IndexError:
            break
        index +=1
    maxcarry = 100 - len(carry)
    if maxcarry == 1:
        maxcarry = 2
    print ans
    print maxcarry
    ans.reverse()
    ans_num = 0
    
    indx2 = 0 
    for c in ans:
        ans_num += c[1]* math.pow(maxcarry,indx2)
        indx2 +=1
    #print "%d"%ans_num
    print "Case #"+str(case_num)+": "+str("%d"%ans_num)
    fout.write("Case #"+str(case_num)+": "+str("%d"%ans_num)+"\n")
    