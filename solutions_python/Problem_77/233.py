'''
Created on 2011/5/7

@author: bletchley
'''

#def findRing(arr,index,used) :
    
    

filename = "../D-large.in"
file = open(filename)

TestN = int(file.readline())
TestCase = 0

while(TestCase<TestN) : 
    num = int(file.readline())
    tok = file.readline().split(' ') 
    arr = []
    used = []
    for i in range(num):
        arr.append(int(tok[i]))
        used.append(False)    
#    print arr    
    
#    flag = False
    count=0
    for i in range(num):
        if(used[i] or i==arr[i]-1):continue
#        flag = True
        long =0;
        pos = i;
        
        while(used[pos]!=True):
           used[pos]=True
           pos = arr[pos]-1 
           long+=1
        count+=long
#    print long , count 
#    if (flag==False):count=0
    TestCase+=1
    ans = "Case #%d: %.6f"%(TestCase,count)   
    print ans
    

