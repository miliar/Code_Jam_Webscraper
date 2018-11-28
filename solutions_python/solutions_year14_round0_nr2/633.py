from math import ceil

def cookie(C,F,X):
    P = (X * F)/C - F
    N = ceil((P-2)/F)
    P = 2
    T = 0
    for i in range(int(N)):
        T += C/P
        P += F
    T += X/P
    return T

def main():
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    N = int(f1.readline().rstrip())
    for i in range(N):
        array = map(float, f1.readline().rstrip().split())
        C = array[0]
        F = array[1]
        X = array[2]
        msg = cookie(C, F, X)
        f2.write("Case #" + str(i+1) + ": " + str(msg) + "\n")

main()
