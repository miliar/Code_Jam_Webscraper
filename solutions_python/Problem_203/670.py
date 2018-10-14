import re

if __name__ == "__main__":
    for _ in range(int(raw_input())):
        n,m = map(int,raw_input().split())
        a = [[str(x) for x in raw_input().strip()] for t in range(n)]
       # print a
        for i in range(n):
            for j in range(m):
                if a[i][j] != "?":
                    for k in range(j - 1, -1, -1):
                        if a[i][k] == "?":
                            a[i][k] = a[i][j]
                        else:
                            break                                 
            for j in range(m - 1, -1, -1):
                if a[i][j] != "?":
                    break
            for k in range(j + 1, m):
                a[i][k] = a[i][j]
        for i in range(n):
            if len(re.findall(r"\?{%d}" % m, "".join(a[i]))) == 0:
                for j in range(i - 1, -1, -1):
                    if len(re.findall(r"\?{%d}" % m, "".join(a[j]))) != 0:
                        a[j] = a[i]
                    else:
                        break
        for i in range(n - 1, -1, -1):
            if len(re.findall(r"\?{%d}" % m, "".join(a[i]))) == 0:
                break
        for j in range(i + 1, n):
            a[j] = a[i]
        print 'Case #%d:' %(_+1)
        for i in range(n):
            print ''.join(a[i])