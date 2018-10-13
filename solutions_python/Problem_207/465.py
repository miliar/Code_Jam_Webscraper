c = {0: 'R', 1: 'Y', 2: 'B'}
pos = {'R': 0, 'Y': 1, 'B': 2}

# returns the character most remaining not ch
def othermax(ch, count, firstch):
    m = -1
    for i in range(len(count)):
        if sum(count) == count[i]: # 0 0 5
            return c[i]
        if pos[ch] == i:
            continue
        if count[i] == m:
            # need to prioritize picking the character at front
            if firstch == c[i]:
                res = firstch
        if count[i] > m:
            res = c[i]
            m = count[i]
    return res

def foo(count):
    i = count.index(max(count)) 
    string = c[i] # char at i
    count[i] -= 1
    while sum(count) > 0:
        newch = othermax(string[-1], count, string[0])
        if newch == string[-1]:
            return "IMPOSSIBLE"
        count[pos[newch]] -= 1
        string += newch

    return string

T = int(input())
for t in range(1, T+1):
    N, R, O, Y, G, B, V = [int(_) for _ in input().split(" ")]
    res = foo([R, Y, B])
    if res[0] == res[-1]:
        res = "IMPOSSIBLE"
    print("Case #{}: {}".format(t, res))