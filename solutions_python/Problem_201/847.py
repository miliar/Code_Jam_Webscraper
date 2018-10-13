#!/usr/bin/env python3

def even(n):
    return n % 2 == 0

def pprint(**kwargs):
    s = " | ".join(k + ": {}" for k in kwargs)
    print(s.format(*list(kwargs.values())))

def solve(i, N, K):
    k = 0
    p = 0
    n = N
    divs = [(N, N)]
    n_a = 1
    n_b = 0
    while True:
        last_k = k
        k += 2**p
        if k >= K:
            #print("breaking on k={}, p={}".format(k, p))
            break
        p += 1

        #b <= a <= b+1, always
        a, b = divs[-1]
        if a == b and even(a):
            #print("a", end=" ")
            new_a, new_b = a//2, a//2 - 1
            n_a = n_a
            n_b = n_a
        elif a == b and not even(a):
            #print("b", end=" ")
            new_a, new_b = a//2, a//2
            n_a = n_a*2
            n_b = 0
        elif a != b and even(a):
            #print("c", end=" ")
            new_a, new_b = a//2, a//2 - 1
            #n_a = (2**p)//4
            #n_b = 3*((2**p)//4)
            n_a = n_a
            n_b = n_a + n_b*2
        elif a != b and not even(a):
            #print("d", end=" ")
            new_a, new_b = a//2, a//2 - 1
            #n_a = 3*((2**p)//4)
            #n_b = (2**p)//4
            n_a = n_a*2 + n_b
            n_b = n_b

        #pprint(p=p, k=k, a=a, b=b, new_a=new_a, new_b=new_b, n_a=n_a, n_b=n_b)
        divs.append((new_a, new_b))


    rem = K - (last_k)
    a, b = divs[-1]
    best = 0
    mid = 0
    worst = 0
    #pprint(N=N, K=K, k=k, rem=rem, a=a, b=b, n_a=n_a, n_b=n_b)
    #print()
    if n_a >= rem:
        if even(a):
            res = a//2, a//2-1
        else:
            res = a//2, a//2
    else:
        if even(b):
            res = b//2, b//2-1
        else:
            res = b//2, b//2

    print("Case #{}: {} {}".format(i, *res))

def main():
    T = int(input())
    for i in range(1, T+1):
        N, K = map(int, input().split(" "))
        solve(i, N, K)

if __name__ == "__main__":
    main()
