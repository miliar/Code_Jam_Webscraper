def attempt(n):
    f = [i for i in range(len(n)-1) if n[i] > n[i+1]]
    if not f:
        return n
    s = f[0]
    g = [i for i in range(s+1) if n[i]==n[s]][0]
    n = n[:g]+chr(ord(n[g])-1)+(len(n)-g-1)*'9'
    return n.split('0')[-1]
t = int(input())
for i in range(1, t + 1):
  n = input()
  print("Case #{}: {}".format(i, attempt(n)))
