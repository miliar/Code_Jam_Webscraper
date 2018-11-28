import glob
import os.path
def procfile(fin,fout):
    T=int(fin.readline())
    
    solutions="\n".join(["Case #%d: %d"%(i+1, procproblem([int(x) for x in fin.readline().split()])) for i in range(T)])
    fout.write(solutions)
    fout.close()

def procproblem(data):
    count=0
    A,B,K=data
    for i in range(A):
        for j in range(B):
            if( i & j < K ):
                count = count + 1
    return count

for x in glob.glob("*.in"):
    if os.path.isfile(x+".out"):
        print(x + ".out already exists")
        continue
    print(x)
    try:
        fin,fout=file(x),file(x+".out","w+")
        procfile(fin,fout)
    finally:
        fin.close()
        fout.close()