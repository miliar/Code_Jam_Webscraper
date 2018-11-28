# Problem C. Bathroom Stalls
# for large input (upto 10**18)

def stringify(l):
    return " ".join(str(d) for d in l)

def solve(n,k):
    res = [0,0]

    if k==n:
        return stringify(res)
    if k == 1:
        mid = (n-1)//2
        m = max(n-1-mid, mid)
        res = [m , n-1-m]
        return stringify(res)


    picked = 0
    while (2*picked + 1) < k :
        picked = 2*picked + 1

    rem = k - picked

    next_level = picked + 1
    parts = (n-picked)//next_level
    excess = (n-picked) - (parts*next_level)

    to_do = 0
    if rem <= excess:
        to_do = parts + 1
    else:
        to_do = parts

    mid = to_do//2
    a,b= mid,to_do-1-mid
    res = [max(a,b), min(a,b)]
    return stringify(res)


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        n,k = map(int,input().split(" "))
        print("Case #{0}: {1}".format(ti + 1, solve(n,k)))
