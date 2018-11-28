import math
def makeun(stri):   
    arr = []
    uni = '' + stri[0]
    counter = 1
    for i in range(1,len(stri)):
        if stri[i]==stri[i-1]:
            counter += 1
        else:
            arr.append(counter)
            counter = 1
            uni += stri[i]
    arr.append(counter)
    return uni,arr
            

T = int(raw_input())
for case in range(1,T+1):
    done = False
    N = int(raw_input())
    freqs = [[] for _ in range(N)]
    sumfreq = []
    unified = ''
    for i in range(N):
        line = raw_input()
        arr = []
        uni,arr = makeun(line)

        freqs[i] = [0]*len(arr)
        for a in range(len(arr)):

            freqs[i][a] = arr[a]
        if len(unified) == 0:
            unified = uni
        elif unified != uni:
            print 'Case #' + str(case) + ': Fegla Won'
            done = True
            break;       
        if len(sumfreq) == 0:
            for s in range(len(arr)):
                sumfreq.append(arr[s])
        else:        
            for j in range(len(arr)):
                sumfreq[j] += arr[j]

    if not done:    
        moves = 0

        for k in range(len(sumfreq)):
            avg = float(sumfreq[k])/float(N)

            xlow = int(math.floor(avg))
            xhi = int(math.ceil(avg))

            movhi = 0
            movlo = 0
            for v in range(len(freqs)):               
                movhi += max(freqs[v][k],xlow)-min(freqs[v][k],xlow)   
                movlo += max(freqs[v][k],xhi)-min(freqs[v][k],xhi)
            moves += min(movlo,movhi)    
        print 'Case #' + str(case) + ': ' + str(moves)    
     
            
        
    

