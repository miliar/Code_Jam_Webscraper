import os
def check_tidy(n):
    N = [int(d) for d in str(n)]
    if N == sorted(N):
        return True
    return False


with open("B-small-attempt0.in","r") as fin:
    T = int(fin.readline())
    i = 0

    while( i < T ):
        N = int(fin.readline())
        for j in xrange(N):
            if check_tidy(N-j):
                print N-j
                fout = open("B-output.txt","a")
                fout.write("Case #"+str(i+1)+": "+str(N-j)+os.linesep)
                break
                
        i+=1 

