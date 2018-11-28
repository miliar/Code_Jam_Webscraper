filename = 'B-small-attempt1';
fin = open(filename + '.in', 'r')
out = open(filename + '.out', 'w')

T = int(fin.readline())

for case in range(1, T+1):
    input = map(lambda x: int(x), fin.readline().split(' '))
    L = input.pop(0)
    t = input.pop(0)
    N = input.pop(0)
    C = input.pop(0)
    
    parsecs = []
    c = 0
    for n in range(0, N):
        parsecs.append(input[c])
        if c == C-1:
            c = 0
        else:
            c += 1
    
    
    if L > 0:
        first = -1
        time = 0
        for n in range(0,N):
            time += parsecs[n] * 2
            if time >= t:
                first = n
                break;
                
        # print first
              
        if first > -1:
            disttime = 0
            for n in range(0, first):
                disttime += parsecs[n] * 2
             
            
            
            
            time = parsecs[first] * 2
            dtime = (t - disttime)
            accS = parsecs[first] - dtime * 0.5
            
            disttime += dtime
            
            # print 'disttime : %d' % disttime
            # print 'accS: %d' % accS
            
            #choose best stats to put accelelators
            leftparscs = [accS] + parsecs[first+1:]
            
            # print leftparscs
            
            
            #find L maxs
            if L > 0:
                maxs = [(-1,0)] * L
                
                for i in range(0, len(leftparscs)):
                    if leftparscs[i] > maxs[0][1]:
                        maxs[0] = ((i, leftparscs[i]))
                        maxs.sort(key=lambda x: x[1])
                    
                
                disttime2 = disttime
                # print maxs
                maxs = dict(maxs)
            else:
                maxs = {}
            
            # print maxs
            
            for i in range(0, len(leftparscs)):
                if maxs.get(i):
                    disttime2 += leftparscs[i]
                else:
                    disttime2 += leftparscs[i] * 2
                    

            out.write('Case #%d: %d\n' % (case, disttime2))
            continue;
            

    print case
    disttime2 = 0
    for i in range(0, len(parsecs)):
        disttime2 += parsecs[i] * 2
                

    out.write('Case #%d: %d\n' % (case, disttime2))    
            
    