def last_tidy(n):
    a = [int(x) for x in n]
    p = 0
    q = 0
    mem = 0
    for i in range(len(a)):
        if a[i]>mem:
            p = i
            q = i
            mem = a[i]
        elif a[i]==mem:
            q = i
        else:
            break
    if q!=len(a)-1:
        a[p] = a[p]-1
        for i in range(p+1, len(a)):
            a[i] = 9
    return int(''.join(map(str, a)))


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = input()
  print("Case #{}: {}".format(i, last_tidy(n)))

