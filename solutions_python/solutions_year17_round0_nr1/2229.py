num = int(input())  # read a line with a single integer
def f(x) :
    if x == "+":
        return 0
    else:
        return 1
def h(l):
    for elem in l:
        if elem != 0:
            return False
    return True
def g(x): return 1-x

def flip(l, i, t, length): 
    #print(l)
    end = i+t
    unchanged = l[0:i]
    newseg = list(map(g, l[i:end]))
    rest = l[end:length]
    #print(unchanged)
    #print(rest)
    #print(newseg)
    unchanged.extend(newseg)
    unchanged.extend(rest)
    return unchanged

for i in range(1, num + 1):
    inp = input().split()
    t = int(inp[1])
    def task():
        count = 0
        l  = list(map(f, list(str(inp[0]))))
        size = len(l)
        for j in range(size):
            if h(l): return str(count)
            elif j+t > size:
                break
            elif l[j] == 0:
                continue
            else:
                l = flip(l, j, t, size)
                count += 1
        if (h(l)) : return str(size)
        return "IMPOSSIBLE"
    print("Case #{}: {}".format(i, task()))
