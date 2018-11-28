import math

N = 10000001

fs = [False] * N
for i in range(1, N):
    if str(i) != str(i)[::-1]:
        continue
    j = i * i
    if str(j) == str(j)[::-1]:
        fs[i] = True
        
in_data = open('C-large-1.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]
res = open('result', 'w')

for case_no in range(T):
    line = in_data[0]
    in_data = in_data[1:]
    A, B = [int(x) for x in line.split()]
    a = int(math.sqrt(A))
    b = int(math.sqrt(B))
    if a*a < A:
        a += 1
    count = sum(fs[a:(b+1)])
    res.write('Case #' + str(case_no+1) + ': ' + str(count) + '\n')