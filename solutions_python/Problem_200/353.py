# Problem B. Tidy Numbers

def solve(ip):
    res = ip[:]
    l = len(ip)

    k = 0
    for i in range(1,l):
        if ip[i] < ip[i-1]:
            k = i
            break

    if k > 0 :
        if ip[k-1] == 1:
            res = [9 for _ in range(l-1)]
        else:
            d = ip[k-1]
            x = 0
            for j in range(k-2,-1,-1):
                if ip[j] != d:
                    break
                else:
                    x += 1

            res[k-x-1] -= 1

            for j in range(k-x,l):
                res[j] = 9

    return "".join(str(d) for d in res)


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        ip = input().strip()
        ip = [int(c) for c in ip]
        print("Case #{0}: {1}".format(ti + 1, solve(ip)))
