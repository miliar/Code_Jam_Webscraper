from sys import stdin

def best(a, b):
    ia, ib, pb = 0, 0, 0
    N = len(a)
    while ia < N and ib < N:
        while ib < N and b[ib] < a[ia]:
            ib += 1
        if ib < N:
            pb += 1
        ia += 1
        ib += 1  
    return pb 

def main():
    T = int(stdin.readline())
    for t in range(T):
        N = int(stdin.readline())
        a = sorted([float(x) for x in stdin.readline().split()])
        b = sorted([float(x) for x in stdin.readline().split()])
        
        print("Case #{}: {} {}".format(t+1, best(b, a), N-best(a,b)))


if __name__ == '__main__':
    main()
