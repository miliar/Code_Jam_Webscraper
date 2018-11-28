#!/usr/bin/python
import sys

def main():
    f = open(sys.argv[1], 'rU')
    t = int(f.readline())

    fout = open(sys.argv[1]+'.out', 'w')

    for case in range(1,t+1):
        N, M = [int(x) for x in f.readline().split()]
        result = processcase(f,N,M)
        fout.write("Case #%(case)d: " %{"case":case})
        fout.write(result)
        fout.write("\n")

    fout.close()
    f.close()


def processcase(fin,N,M):
    lawn = [[int(x) for x in fin.readline().split()] for _ in range(N)]
    
    if ((N == 1) or (M == 1)):
        return "YES"
    
    for line in range(N):
        for col in range(M):
            if (lawn[line][col] < max(lawn[line])):
                if (lawn[line][col] < max(column(lawn,col))):
                    return "NO"
           
    
    return "YES"
            
def column(lawn,col):
    for line in lawn:
        yield line[col]


if __name__ == '__main__':
    main()

