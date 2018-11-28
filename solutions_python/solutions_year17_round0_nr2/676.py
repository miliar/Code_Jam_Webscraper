import sys
f = open('B-large.in') 
#f = sys.stdin
#sys.stdout = open('A-small-practice.out', 'w')   

#f = open('A-large-practice.in') #sys.stdin
sys.stdout = open('B-large.out', 'w')   

T = int(f.readline().strip())


for k in range(T):
    st = f.readline().strip().split()
    
    a = [int(s) for s in st[0]]    
    #print(a)

    lastD  = 9
    for i in range(len(a) - 1, -1, -1):
        if a[i] > lastD:
            #print(i, a[i])
            a[i] -= 1
            for j in range(i + 1, len(a)):
                a[j] = 9
        lastD = a[i] 
    #print(a)

    begin_l = True
    res = ''
    for it in a:
        if not (begin_l and it == 0):
            res += str(it)
            begin_l = False
        
    print('Case #' + str(k+1) + ': ' + res)
        
f.close()   


