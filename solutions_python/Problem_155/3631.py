import sys

def test(A):
    count = 0
    need = 0
    for i in range(0, len(A)):
        if A[i] != 0:
            if i > (count + need):
                need = i - count
            count = count + A[i]

    return need

def unit():
    print test([1, 1, 1, 1])
    print test([0, 9])
    print test([1 ,1, 0, 0, 1, 1])
    print test([1])
    print test([1, 1, 0, 3, 0, 0, 0, 1])

def main():
    result = []
    iters = sys.stdin.readline().strip()
    for i in range(0, int(iters)):
        A = []
        S = sys.stdin.readline().strip().split()
        for j in range(0, int(S[0])+1):
            A.append(int(S[1][j]))
        result.append(test(A))

    for i in range(0, len(result)):
        print("Case #%d:" % (i+1)), result[i]

if __name__=="__main__":
    main()