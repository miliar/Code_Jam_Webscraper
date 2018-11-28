from math import sqrt
import time

def read_file(filepath):
    try:
        lines = file(filepath, 'rU').readlines()
    except IOError, e:
        print '*** file open failed:', filepath
        raise e
    else:
        return lines

def get_fact(n1, n2=1):
    a = 1
    for i in range(n2, n1+1):
        a *= i
        #a = cut(a)
        
        #print a
    return a

def get_comb(n, k):
    a = get_fact(n, k+1)
    a /= get_fact(n-k)
    #print a
    return a

def cut(n):
    if n>1000:
        a = n%1000
        if a==0:
            return 1000
        else:
            return a
    else:
        return n
    
# main
t0 = time.time()

#filepath = './test'
filepath = './A-small-attempt0'
filepath = './A-large'
lines = read_file(filepath+'.in')
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\r\n')
print lines

N = int(lines[0])
answers = []
i = 1
for m in range(N):
    # read a case
    P, K, L = lines[i].split(' ')
    i += 1
    P = int(P)
    K = int(K)
    L = int(L)
    print P, K, L
    
    freq = lines[i].split(' ')
    i += 1
    for j in range(L):
        freq[j] = int(freq[j])
    freq.sort(reverse=True)
    print freq
    
    ans = 0
    k = 0
    p = 1
    for j in range(L):
        ans += p*freq[j]
        k += 1
        if k==K:    
            k = 0
            p += 1
            
    answers.append(ans)
    #print n, a, b, ans, digit[-3:]
    
# answers
try:
    f = file(filepath+'.out', 'w')
except IOError, e:
    print 'cannot open:', filepath
    raise e
else:
    pass
    
for m in range(N):
    answers[m] = 'Case #'+str(m+1)+': ' + str(answers[m])
    f.write(answers[m] + '\n')
    print answers[m]

# elapsed time
t = time.time() - t0
m = int(t/60)
s = t - 60*m
print m,'min', s, 'sec'