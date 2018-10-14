# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:56:55 2017

@author: Abhishek
"""



def flip(pcpnstr, idx, k):
    pcpn = list(pcpnstr)
    for i in range(k):
        if pcpn[idx+i]=='+':
            pcpn[idx+i]='-'
        else:
            pcpn[idx+i]='+'
    return ''.join(pcpn)


def runMain(caseStr):
    caseStr = caseStr.split()
    pcpn = caseStr[0]
    fliplen = int(caseStr[1])
    flips=0
    idx=0
    while idx <= len(pcpn)-fliplen:
        i=idx

        while not pcpn[i]=='-' and i < len(pcpn)-fliplen:
            i+=1
        
        if pcpn[i] == '-':    
            pcpn = flip(pcpn, i, fliplen)
            flips+=1
        else:
            break
        
        if not i==idx:
            idx=i
        else:
            idx+=1
    
    if pcpn.count('-')>0:
        return False,0
    else:
        return True,flips
    


if __name__ == "__main__":
    inputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\A-large.in'
    outputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\A-large.out'
    answers=[]
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for i in range(numCases):
            line = f.readline()
            ok, answer = runMain(str(line))
            if ok:
                answers.append(answer)
            else:
                answers.append('IMPOSSIBLE')
    with open(outputFile, 'w') as wf:
        for i in range(len(answers)):
            wf.write("Case #"+str(i+1)+": "+str(answers[i])+"\n")




