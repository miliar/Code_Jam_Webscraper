import sys
f = open('A-large.in') 
#f = sys.stdin
#sys.stdout = open('A-small-practice.out', 'w')   

#f = open('A-large-practice.in') #sys.stdin
sys.stdout = open('A-large-attempt.out', 'w')   

T = int(f.readline().strip())


for k in range(T):
    st = f.readline().strip().split()
    a = [1 if s == '+' else 0 for s in st[0]]
    #print(a)
    K = int(st[1])

    step = 0
    for i in range(len(a) - K + 1):
        if a[i] == 0:
            step += 1
            for j in range(i, i + K):
                a[j] = 1 - a[j]
            #print(a)
    
    br = False
    for i in range(len(a) - K, len(a)):
        if a[i] < 1:
            br = True

    if br:
        print('Case #' + str(k + 1) + ': ' + 'IMPOSSIBLE')
    else:        
        print('Case #' + str(k + 1) + ':', str(step))
        
f.close()   


