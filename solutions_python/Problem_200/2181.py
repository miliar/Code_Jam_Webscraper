# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def isTidy(digits):
    i=0
    for i in range(len(digits)-1):
        if digits[i]>digits[i+1]:
            return False,i
    return True,i
        
print isTidy([1,4,3,3])    
    
def runTidy(digits):
    ok, i = isTidy(digits)
    print ok, i
    if ok:
        print digits
        return int(''.join(str(bit) for bit in digits))
    else:
        print digits
        digits[i]-=1
        while i<=len(digits)-2:
            digits[i+1]=9
            i+=1
        return runTidy(digits)

print runTidy([3,0,0,1])
        
def runMain(n):
    digits=[]
    if n==0:
        digits = [0]
    else:
        while n>0:
            digit=n%10
            digits.insert(0,digit)
            n=n/10
    print digits
    return runTidy(digits)
        
if __name__ == "__main__":
    inputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\B-large.in'
    outputFile = 'C:\Users\Abhishek\Documents\Python Scripts\codejam\B-large.out'
    answers=[]
    with open(inputFile, 'r') as f:
        numCases = f.readline()
        for line in f.readlines():
            answers.append(runMain(int(line)))
    with open(outputFile, 'w') as wf:
        for i in range(len(answers)):
            wf.write("Case #"+str(i+1)+": "+str(answers[i])+"\n")
        
    
    
    
    
    
    
    