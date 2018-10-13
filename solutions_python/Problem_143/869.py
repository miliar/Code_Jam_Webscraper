import os
import sys
os.chdir("E:\CODEX 5.0\codex 6.0")
sys.stdin = open('input.in','r')
sys.stdout = open('output.out','w+')
t = int(input())
temp = 0;
try:
        
    while(temp<=t):
        li1 = (input().split(" "))
        a = int(li1[0]);
        b = int(li1[1]);
        k = int(li1[2]);
        counter = 0
        r = 0
        for p in range(a):
            for q in range(b):
                if(int((p) &(q))<k):
                    counter = counter + 1;
            
        temp = temp + 1;
        print('Case #{CaseNo}: '.format(CaseNo=temp),end="")
        print(counter)
except EOFError:
    pass;



    
