def solve(X, files):
    files = sorted(files)
    count = 0
    while len(files) > 0:
        a = files.pop()
        found = None
        for i,b in enumerate(files):
            if a + b > X:
                break
            found = i
        if found is not None:
            files.pop(found)
        count += 1
    return count

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        N,X = map(int, raw_input().split())
        files = map(int, raw_input().split())
        print "Case #%d: %d" % (i, solve(X, files))
            
