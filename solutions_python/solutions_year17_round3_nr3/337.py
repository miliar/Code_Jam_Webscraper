from functools import reduce

def shareU(llCores, u, n, k):
    llCores = sorted(llCores, reverse=True)
    bestCores = sorted(llCores[:k])
    worstCores = llCores[k:]

    s = sum(bestCores[:1])
    i = 1
    while i < len(bestCores) and (s + u) / i > bestCores[i]:
        i += 1
        s = sum(bestCores[:i])

    bestCores[:i] = [(sum(bestCores[:i]) + u) / i] * i

    return bestCores + worstCores

def solve(llCores, k):
    pr = reduce(lambda x, y: x*y, llCores[:k], 1)
    return pr

t = int(input())
for i in range(1, t+1):
    line = input()
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])
    u = float(input())
    llCores = [float(elem) for elem in input().split(" ")]
    llCores = shareU(llCores, u, n, k)
    # print(llCores)
    print("Case #{}: {}".format(i, solve(llCores, k)))