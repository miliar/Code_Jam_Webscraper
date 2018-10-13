

def find_tidy(n):
    n = map(lambda x: int(x), list(str(n)))
    m = len(n)
    for i in range(m-1,0,-1):
        if n[i-1]>n[i]:
            n[i-1] -= 1
            n[i:m] = [9]*(m-i)
    res = 0
    for i in range(0, m):
        res += n[m-i-1]*10**i
    return res

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for i in xrange(1, T + 1):
      n = f.readline().strip()
      print "Case #{}: {}".format(i, find_tidy(n))



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
