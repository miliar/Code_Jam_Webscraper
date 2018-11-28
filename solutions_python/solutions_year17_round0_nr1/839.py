def solve(s, k):
    l = len(s)
    tmp = [0] * l
    count = 0
    for n in range(l-k+1):
        if s[n] == '-' and tmp[n]%2 == 0:
            for i in range(n,n+k):
                tmp[i] += 1
            count += 1
        if s[n] == '+' and tmp[n]%2 == 1:
            for i in range(n,n+k):
                tmp[i] += 1
            count += 1
    for j in range(l-k+1, l):
        if s[j] == '-' and tmp[j]%2 == 0:
            count = 'IMPOSSIBLE'
            break
        if s[j] == '+' and tmp[j]%2 == 1:
            count = 'IMPOSSIBLE'
            break

    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        s, k = input().split(" ")
        k = int(k)
        count = solve(s, k)
        print("Case #{}: {}".format(i, count))