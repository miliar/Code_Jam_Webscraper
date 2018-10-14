import sys
f = open('A-large.in') 
#f = sys.stdin
#sys.stdout = open('A-small-practice.out', 'w')   

#f = open('A-large-practice.in') #sys.stdin
sys.stdout = open('A-large-practice.out', 'w')   

T = int(f.readline().strip())


for k in range(T):
    st = f.readline().strip().split()
    ns = int(st[0])
    S = st[1] 
    w = 0
    Aud = 0
    for i in range(1, len(S)):
        Aud += int(S[i-1])
        if Aud < i:
            w += 1
            Aud += 1

    print('Case #' +str(k+1) + ':', str(w))
        
f.close()   


