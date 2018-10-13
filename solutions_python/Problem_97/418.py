fin = open('C-small-attempt0.in', 'r')
fout = open('cycle.txt', 'w')

seq = {}
seq[1] = 1
for i in range(2,10):
    seq[i] = seq[i-1] + i

def counting(a,b):
    d = [0 for i in range(b+1)]
    ans = [] 
    for i in range(a, b+1):
        if d[i] != 1:
            s = str(i)
            num = 0
            for j in range(1,len(s)):
                inv = s[-j:] + s[:-j]
                invnumb = int(inv)
                if a <= invnumb <= b:                    
                    if d[invnumb] == 1:
                        continue
                    if i != invnumb:
                        num += 1
                        d[i] = 1
                        d[invnumb] = 1
            if num != 0:
                ans.append(num)
    return ans

T = int(fin.readline())
for i in range(T):
    s = fin.readline()
    A, B = map(int, s.split())
    temp = counting(A, B)
    answer = 0
    for j in temp:
        answer += seq[j]
    fout.write('Case #' + str(i+1) + ': ' + str(answer) + '\n')
    
fin.close()
fout.close()
