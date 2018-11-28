import fileinput
f = fileinput.input()

def flipped(x,i,k):
    j = 0
    while j<k:
        if x[j+i]==0:
            x[j+i] = 1
        else:
            x[j+i] = 0
        j += 1
    return x

t = input()
c = 1
while t:
    t -= 1
    [s,k] = raw_input().split()
    k = int(k)
    state = [0 for _ in xrange(len(s))]
    i = 0
    while i<len(s):
        if s[i]=='+':
            state[i] = 1
        i += 1
    statevisited = {}
    q = [[state, 0]]
    flag = 0
    while len(q)>0:
        [curstate, l] = q.pop(0)
        #print curstate, l
        if sum(curstate) == len(s):
            print 'Case #'+str(c)+': '+str(l)
            flag = 1
            break
        try:
            statevisited[str(curstate)] += 1
        except:
            statevisited[str(curstate)] = 1
            i = 0
            while i<len(curstate):
                if curstate[i]==0:
                    j = 0
                    while j<k:
                        if i-j>=0 and i-j+k<=len(curstate):
                            nextstate = flipped(curstate[:],i-j,k)[:]
                            #print curstate, nextstate, i,j,k,l
                            q.append([nextstate,l+1])
                        j += 1
                i += 1

    if flag==0:
        print 'Case #'+str(c)+': '+'IMPOSSIBLE'
    c += 1
                
        
