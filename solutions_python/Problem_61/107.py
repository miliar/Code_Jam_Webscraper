import re, sys, os

def fact(n):
    if(n==0): return 1
    else: return n*fact(n-1)
def comb(n,r):
    return fact(n)/(fact(r)*fact(n-r))

counts= {}

modder=100003


def enum_n(n, r):
    #n = number, r - needed rank
    global counts
    print "recd:", n , r 
    if(r==1): return 1
    else:
        if(n in counts and r in counts[n] and counts[n][r]!=-1):return counts[n][r]
        if(n not in counts): counts[n]={}
        if(r not in counts[n]): counts[n][r]=-1

        tot = 0
        #r,r-1 - r,r-2,    stop 
        for i in range(n-r):
            if(r-(i+1)==0):break
            print "CaLL:",r,",",r-(i+1)
            if(r not in counts): counts[r]={}
            if(r-(i+1) not in counts[r]): counts[r][r-(i+1)]=-1
            if(counts[r][r-(i+1)]==-1): counts[r][r-(i+1)]= enum_n(r,r-(i+1))
            print  counts[r][r-(i+1)]
            if(i !=0):
                tot += comb(n-r-1,i) * counts[r][r-(i+1)]
            else:
                tot += counts[r][r-(i+1)]
            if(tot>modder):tot=tot%modder      
        counts[n][r] =tot
        return counts[n][r]

            #enum_n(r,r-(i+1))  
       
def process(n):
    global counts
    counts.clear()
    tot=0
    for i in range(1,n):
        counts.clear()
        #print "Calling:",n,i
        x=enum_n(n,i)
        print "Calling:",n,i,x

        tot+=x

    print "Ways:", tot
    return tot%modder



def fp():
    f=open(sys.argv[1])
    lineno=0
    case=0
    for line in f:
        lineno+=1
        if(lineno==1):continue
        a=int(line.strip())
        case+=1
        temp = process(a)
        print "Case #%d: %d"%(case, temp)


    f.close()


fp()
