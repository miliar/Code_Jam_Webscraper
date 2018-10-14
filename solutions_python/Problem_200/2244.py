def untidy(x):
    s = str(x)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return i
    return -1

def zafter(x, n):
    s = list(str(x))
    for i in range(n+1, len(s)):
        s[i] = '0'
    return int(''.join(s)) - 1

count = int(raw_input())
for cur in range(count):
    x = int(raw_input())
    while untidy(x) != -1:
        x = zafter(x, untidy(x))
    print("Case #{}: {}".format(cur+1, x))
