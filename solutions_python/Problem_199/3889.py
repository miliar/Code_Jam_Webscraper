INF = 10000

number = int(input())
rj = []

def rek(pan, i, size, count=0) :
    if '-' not in pan :
        return 0
    if count == 20 :
        return INF
    index = i % len(pan)
    if size-1 + index >= len(pan) :
        return rek(pan[:], i+1, size, count+1)
    return min(
            rek(apply(pan[:], index, size), i+size-1, size, count+1)+1, 
            rek(pan[:], i+1, size, count+1)
        )

def apply(pan, pos, size) :
    for i in range(pos, pos+size) :
        pan[i] = opposite(pan[i])
    return pan

def opposite(char) :
    if char == '+' :
        return '-'
    return '+'

while number > 0 :
    number-=1
    inp = input().split()
    pan = list(inp[0])
    size = int(inp[1])
    rj.append(rek(pan, 0, size))

for i, val in enumerate(rj) :
    if val == INF :
        msg = "Case #" + str(i+1) + ": " + "IMPOSSIBLE"
    else :
        msg = "Case #" + str(i+1) + ": " + str(val)
    print(msg)