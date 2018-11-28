
def flip(arr):
    res = []
    for i in arr:
        res.append('+' if i=='-' else '-')
    return res

def pancake(s, k):
    s = list(s)
    i, n, counter = 0, len(s), 0    
    while i+k<=n:
        if s[i]=='+':
            i +=1
            continue
        else:
            s[i:(i+k)]= flip(s[i:(i+k)])
            counter += 1
            i += 1
    return 'IMPOSSIBLE' if '-' in s else counter


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for i in xrange(1, T + 1):
      s, k = f.readline().strip().split(" ")
      print "Case #{}: {}".format(i, pancake(s, int(k)))
