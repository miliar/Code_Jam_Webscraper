

def tidy(k):
    for i in range(1, len(k)):
        if k[i-1] > k[i]:
            return i-1
    return -1

def solve(k):
    i = tidy(k)
    if i == -1:
        return int(''.join(str(c) for c in k))
    assert k[i] > 0
    k[i] = k[i] - 1
    for j in range(i+1, len(k)):
        k[j] = 9
    return solve(k)

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
      s = input()
      print("Case #{}: {}".format(i, solve([int(c) for c in s])))
