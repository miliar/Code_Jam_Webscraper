import fileinput

__author__ = 'psmit'



def main():
    inp = fileinput.input()

    T = int(inp.readline())

    for t in range(1,T+1):
        A,B,K = (int(x) for x in inp.readline().split())
        count = 0
        for i in range(A):
            for j in range(B):
                if i & j < K:
                    count += 1

        print("Case #{}: {}".format(t, count))



main()