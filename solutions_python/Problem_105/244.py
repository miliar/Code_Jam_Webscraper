#!/usr/bin/python
# Filename:Problem A. Diamond Inheritance.py
import sys,time

strFile = "Problem A. Diamond Inheritance"
strFileSmall = "Problem A. Diamond Inheritance small"
strFileLarge = "Problem A. Diamond Inheritance large"

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
    N = read_int(f)
    Tn = [[] for row in range(N)]

    for i in range(N):
        Ti = read_ints(f)
        for j in range(Ti[0]):
            Tn[Ti[j+1] - 1].append(i)

    return (N,Tn)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def travel(listN,i,Tn):
    
    for j in range(len(Tn[i])):
        if(1 == listN[Tn[i][j]]):
            if debug:
                print(i)
                print(Tn[i][j])
            return 1
        else:
            if (1 == travel(listN,Tn[i][j],Tn)):
                return 1
            listN[Tn[i][j]] = 1
            
    return 0

def solve_small(case):
    N,Tn = case
    if debug:
        print(Tn)
    #return ("No")
    res = 0
    for i in range(N):
        listN = [0 for row in range(N)]
        res = travel(listN,i,Tn)
        if(res):
            break
    
    if(1 == res):
        return ("Yes")
    else:
        return ("No")

##def solve_large(case):

solve_large = solve_small

################################################################################

start_time = time.time()

FAIL = 'Too Bad'
debug = True
#debug = False

#solve(solve_small,strFile)
solve(solve_small,strFileSmall)
#solve(solve_large,strFileLarge)

total_time = time.time() - start_time
print("All Completed in %.1f seconds" % total_time)
