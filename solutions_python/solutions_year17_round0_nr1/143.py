# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  
    p, k = raw_input().split(" ")  # read a list of integers, 2 in this case
    k = int(k)
    p = list(p)
    ret = 0
    for j in range(len(p)):
        if p[j] == '-':
            if j + k > len(p):
                ret = 'IMPOSSIBLE'
                break
            ret += 1
            for c in range(k):
                if p[j + c] == '-':
                    p[j + c] = '+'
                else:
                    p[j + c] = '-'
    print("Case #{}: {}".format(i, str(ret)))
    # check out .format's specification for more formatting options


