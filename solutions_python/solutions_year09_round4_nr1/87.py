'''
def subsolve(vs,start_index,count,start_value):
    """Count how many moves are needed to ensure the
    subrange from start_index of count elements has
    values below start_value+index."""
    moves=0
    for index in xrange(start_index, start_index+count):
        if vs[index]>start_value+index:
            offset = vs[index]-start_value-index
            # Wants to move down offset rows.
            # First ensure next offset rows are okay to move up.
            subsolve(vs,index+1,offset,start_value+index)
   '''         
def process(vs):
    ks=[None]*len(vs)
    for i in xrange(len(vs)):
        ii=i+1
        for j in xrange(len(vs)):
            if vs[j]<=ii and ks[j] is None:
                ks[j] = i
                break
    #print list(zip(vs,ks))
    moves = 0
    isdone=False
    while not isdone:
        isdone=True
        old_moves=moves
        for i in xrange(len(ks)-1):
            if ks[i]>i or ks[i+1]<i+1:
                isdone=False
            if ks[i]>i and ks[i+1]<i+1:
                #print "swap {0} and {1}".format(i,i+1)
                ks[i],ks[i+1] = ks[i+1],ks[i]
                moves+=1
        if not isdone and old_moves==moves:
            #No progress. Do anything:
            for i in xrange(len(ks)-1):
                if ks[i+1]<i+1:
                    #print "SWAP {0} and {1}".format(i,i+1)
                    ks[i],ks[i+1] = ks[i+1],ks[i]
                    moves+=1
                    break
    return moves
"""
def solve(vs):
    count=0
    stack = list(reversed(range(len(vs))))
    while len(stack)>0:
        i = stack.pop()
        if i==len(vs)-1:
            continue
        if vs[i]>i+1:
            #Wants to move up
            if vs[i+1]>i+1:
                #Can't
                assert vs[i+1]==i+2
                if vs[i+1]==vs[i]:
                    print "sneaky"
                    vs[i+1]+=1
                else:
                    print "SWAP {0}, {1}".format(i,i+1)
                    vs[i],vs[i+1]=vs[i+1],vs[i]
                    count+=1
                stack.append(i)
                stack.append(i+1)
            else:
                print "swop {0}, {1}".format(i,i+1)
                vs[i],vs[i+1]=vs[i+1],vs[i]
                count+=1
    return count"""

cases = int(raw_input().strip())
for c in range(cases):
    n = int(raw_input().strip())
    vs=[]
    for i in range(n):
        s = raw_input().strip()
        vs.append(s.rfind("1")+1)
    print "Case #{0}: {1}".format(c+1, process(vs))
    
    #answer = solve(vs)
    #print "Case #{0}: {1}".format(c+1, answer)
    
