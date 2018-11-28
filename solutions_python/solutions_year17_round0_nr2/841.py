
def cal(n):
    for i in range(len(n)-1,0,-1):
        if n[i] < n[i-1]:
            n = n[:i] + '9'*(len(n) - i)
            n = n[:i-1] + chr(ord(n[i-1]) -1) + n[i:]
    return int(n.lstrip("0"));


t = int(raw_input())

for i in range(t):
    n = raw_input()
    result = cal(n)
    print("Case #{}: {}".format(i+1,result))