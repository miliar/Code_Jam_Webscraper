import re

if __name__ == "__main__":
    with open("a-large.txt", "r") as r, open("a-large-out.txt", "w") as w:
        t = int(r.readline().strip())
        for _ in range(t):
            x,y = map(int, r.readline().strip().split())
            arr = []
            for a in range(x):
                arr.append(list(r.readline().strip()))
            for a in range(x):
                for b in range(y):
                    if arr[a][b] != "?":
                        for c in range(b - 1, -1, -1):
                            if arr[a][c] == "?":
                                arr[a][c]=arr[a][b]
                            else:
                                break
                for b in range(y-1,-1,-1):
                    if arr[a][b] != "?":
                        break
                for c in range(b+1,y):
                    arr[a][c]=arr[a][b]
            for a in range(x):
                if len(re.findall(r"\?{%d}" % y, "".join(arr[a]))) == 0:
                    for b in range(a-1,-1,-1):
                        if len(re.findall(r"\?{%d}" % y, "".join(arr[b]))) != 0:
                            arr[b]=arr[a]
                        else:
                            break
            for a in range(x-1,-1,-1):
                if len(re.findall(r"\?{%d}" % y, "".join(arr[a]))) == 0:
                    break
            for b in range(a+1,x):
                arr[b]=arr[a]
            w.write("Case #%d:\n" % (_ + 1))
            for a in range(x):
                w.write("".join(arr[a]) + "\n")