
import fileinput

def solveD(A,B):
    C = sorted(zip(A,[0]*len(A))+zip(B, [1] *len(B)), key = lambda x: x[0])
    
    aux = 0
    loses = 0
    for i in range(len(C)):
        if C[i][1] == 1:
            aux += 1
        elif C[i][1] == 0:
            aux -= 1
        if aux < 0:
            loses += 1
            aux = 0
    jane_wins_trick = len(A)-loses
    
    aux = 0
    for i in range(len(C)):
        if C[i][1] == 0:
            aux += 1
        if aux > 0 and C[i][1] == 1:
            aux -= 1
    jane_wins_normal = aux
            
    return jane_wins_trick, jane_wins_normal

def main():
    fin = fileinput.input()
    T = int(next(fin)) # number of test cases
    for case in range(1, T+1):
        N = int(next(fin)) # number of blocks
        A = [float(x) for x in next(fin).split(" ")]
        B = [float(x) for x in next(fin).split(" ")]
        R1,R2 = solveD(A, B)
        print("Case #{}: {} {}".format(case,R1,R2))
    fin.close()

if __name__ == '__main__':
    main()
