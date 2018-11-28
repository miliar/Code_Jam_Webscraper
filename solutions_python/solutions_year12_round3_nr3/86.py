#!/usr/bin/python
# Filename:Problem C. Box Factory.py
import sys,time

strFile = "Problem C. Box Factory"
strFileSmall = "Problem C. Box Factory small"
strFileLarge = "Problem C. Box Factory large"

def read_word(f):
    return f.readline().strip()

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_int(f, b=10):
    return int(read_word(f), b)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_float(f):
    rdStr = f.readline()
    return float(rdStr)

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]
    
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res

def solve(solver,file):
    inFile = open(file+".in")
    assert inFile
    outFile = open(file+".out",'w')
    assert outFile

    T = read_int(inFile)
    for n in range(T):
        case = read_case(inFile)
        
        if debug:
            print("case %d inPut:"%(n+1))
            print(case)
            print("\n")
            
        res = solver(case)
        write_case(outFile, n+1, res)
        if debug:
            print("case %d outPut:"%(n+1))
            print(res)
            
        total_time = time.time() - start_time
        print("\nCase #%d Completed in %.1f seconds" % (n+1, total_time))
        print("###############################################################")

    inFile.close()
    outFile.close()

################################################################################

def read_case(f):
    NM = read_ints(f)
    Nlist = read_ints(f)
    Mlist = read_ints(f)
    return (NM,Nlist,Mlist)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def SubSolve(t,b,nexti,nextj,tLeft,bLeft,N,M,Nlist,Mlist):
    ret = 0
    if(t != b):
        ret1 = 0
        ret2 = 0
        if(N == nexti):
            ret1 = 0
        else:
            ret1 = SubSolve(Nlist[nexti*2 + 1],b,nexti + 1,nextj,Nlist[nexti*2],bLeft,N,M,Nlist,Mlist)

        if(M == nextj):
            ret2 = 0
        else:
            ret2 = SubSolve(t,Mlist[nextj*2 + 1],nexti,nextj + 1,tLeft,Mlist[nextj*2],N,M,Nlist,Mlist)
            
        if(ret2 > ret1):
            ret = ret2
        else:
            ret = ret1

    else:
        if(tLeft > bLeft):
            ret += bLeft
            if(M == nextj):
                ret += 0
            else:
                ret += SubSolve(t,Mlist[nextj*2 + 1],nexti,nextj + 1,tLeft - bLeft,Mlist[nextj*2],N,M,Nlist,Mlist)
        elif(tLeft < bLeft):
            ret += tLeft
            if(N == nexti):
                ret += 0
            else:
                ret += SubSolve(Nlist[nexti*2 + 1],b,nexti + 1,nextj,Nlist[nexti*2],bLeft - tLeft,N,M,Nlist,Mlist)
        else:
            ret += tLeft
            if(N == nexti or M == nextj):
                ret += 0
            else:
                ret += SubSolve(Nlist[nexti*2 + 1],Mlist[nextj*2 + 1],nexti + 1,nextj + 1,Nlist[nexti*2],Mlist[nextj*2],N,M,Nlist,Mlist)
    #print(ret)
    return ret     
def solve_small(case):
    NM,Nlist,Mlist = case
    N = NM[0]
    M = NM[1]
    res = 0
    for i in range(0,N):
        ret = SubSolve(Nlist[i*2 + 1],Mlist[1],i+1,1,Nlist[i*2],Mlist[0],N,M,Nlist,Mlist)
        #print(ret)
        #print("\n\n")
        if ret > res:
            res = ret
            
    return res

##def solve_large(case):

solve_large = solve_small

################################################################################

start_time = time.time()

FAIL = 'Too Bad'
#debug = True
debug = False

#solve(solve_small,strFile)
solve(solve_small,strFileSmall)
#solve(solve_large,strFileLarge)

total_time = time.time() - start_time
print("All Completed in %.1f seconds" % total_time)
