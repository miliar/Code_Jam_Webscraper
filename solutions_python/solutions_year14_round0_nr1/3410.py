'''
Created on Apr 11, 2014

@author: shaqal
'''


T = int(raw_input())

for i in range(0,T):
    ans1=0
    ans2=0
    a=[[],[],[],[]]
    b=[[],[],[],[]]
    ans1 = int(raw_input()) -1
    for j in range(0,4):
        a[j] = raw_input().split()
        
    ans2 = int(raw_input()) -1
    for j in range(0,4):
        b[j] = raw_input().split()
        

    a[ans1] = sorted(a[ans1])
    b[ans2] = sorted(b[ans2])
    
    match =0
    matched = 1
    j=0
    k=0
    while(j!=4 and k!=4):
        if a[ans1][j]<b[ans2][k]:
            j+=1
        else:
            if a[ans1][j]>b[ans2][k]:
                k+=1
            else:
                matched = int(a[ans1][j])
                match +=1
                j+=1
                k+=1
    
    if match == 0:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    if match == 1:
        print "Case #"+str(i+1)+": "+str(matched)
    if match >1:
        print "Case #"+str(i+1)+": Bad magician!"
    
    
    