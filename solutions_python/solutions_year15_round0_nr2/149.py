# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Problem 1
input_file = open(input("input from: "), "r")
output_file = open(input("output to: "), "w")
T = int(input_file.readline().strip())
for i in range(T):
    S = input_file.readline().strip().split()[1]
    c_sum = 0
    result = 0
    for d in range(len(S)):
        if S[d]!='0' and d>c_sum:
            result += d-c_sum
            c_sum = d
        c_sum += int(S[d])
    output_file.write("Case #"+str(i+1)+": "+str(result)+"\n")
input_file.close()
output_file.close()

# <codecell>

#Problem 2
input_file = open(input("input from: "), "r")
output_file = open(input("output to: "), "w")
T = int(input_file.readline().strip())
for i in range(T):
    D = int(input_file.readline().strip())
    P = list(map(int, input_file.readline().strip().split()))
    block_size = 2
    max_time = max(P)
    cur_time = max_time
    while block_size<max_time:
        total = 0
        for p in P:
            total += (p-1)//block_size
        cur_time = min(cur_time, total+block_size)
        block_size += 1
    output_file.write("Case #"+str(i+1)+": "+str(cur_time)+"\n")
input_file.close()
output_file.close()

# <codecell>

#Problem 3
import numpy as np

input_file = open(input("input from: "), "r")
output_file = open(input("output to: "), "w")
i = [[0,-1,0,0], [1,0,0,0], [0,0,0,-1], [0,0,1,0]]
j = [[0,0,0,-1], [0,0,-1,0], [0,1,0,0], [1,0,0,0]]
k = [[0,0,1,0], [0,0,0,-1], [-1,0,0,0], [0,1,0,0]]
neg_one = np.dot(i,i)
one = np.dot(neg_one, neg_one)
T = int(input_file.readline().strip())
def IandJ(s, n):
    if n%4==0:
        return 'NO'
    s = s*(4 if n >= 4 else n);
    result = one;
    for c in range(len(s)):
        result = np.dot(result, eval(s[c]));
        if np.all(result==i):
            break;
    else:
        return 'NO'
    result = one;
    rev_s = s[::-1];
    for p in range(len(rev_s)):
        result = np.dot(result, eval(rev_s[p]));
        if (np.all(result==np.transpose(k)) or (p==0 and np.all(result==k))) and p+c+2<n*len(s):
            return 'YES'
    else:
        return 'NO'
    
for pupu in range(T):
    [L, X] = input_file.readline().strip().split()
    [L, X] = int(L), int(X)
    result = one
    S = input_file.readline().strip()
    for c in S:
        result = np.dot(result, eval(c))
    if np.all(result==one):
        result = 'NO'
    elif np.all(result==neg_one):
        if X%2==0:
            result = 'NO'
        else:
            result = IandJ(S, X)
    else:
        if X%2 or (X//2)%2==0:
            result = 'NO'
        else:
            result = IandJ(S, X)
    output_file.write("Case #"+str(pupu+1)+": "+result+"\n")
input_file.close()
output_file.close()

# <codecell>

#Problem 4
input_file = open(input("input from: "), "r")
output_file = open(input("output to: "), "w")
T = int(input_file.readline().strip())
for i in range(T):
    X,R,C = [int(j) for j in input_file.readline().strip().split()]
    R,C = (C,R) if C<R else (R,C)
    if X>=7 or (R*C)%X:
        result = 'RICHARD'
    elif C<X or R<(X+1)//2 or (X>3 and R==(X+1)//2):
        result = 'RICHARD'
    elif X<5:
        result = 'GABRIEL'
    elif X==5:
        if R==3 and C==5:
            result = 'RICHARD'
        else:
            result = 'GABRIEL'
    else:
        result = 'GABRIEL'
    output_file.write("Case #"+str(i+1)+": "+str(result)+"\n")
input_file.close()
output_file.close()

# <codecell>

def test(s):
    result = one
    for haha in s:
        result = np.dot(result, eval(haha))
    if np.all(result==i):
        return 'i'
    elif np.all(result==np.negative(i)):
        return '-i'
    elif np.all(result==j):
        return 'j'
    elif np.all(result==np.negative(j)):
        return '-j'
    elif np.all(result==k):
        return 'k'
    elif np.all(result==np.negative(k)):
        return '-k'
    elif np.all(result==one):
        return '1'
    elif np.all(result==neg_one):
        return '-1'
    return result

