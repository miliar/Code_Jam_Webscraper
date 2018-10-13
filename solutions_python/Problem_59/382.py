#!/usr/bin/pyhton

def find(item, l):
    for x in l:
        if item == x:
            return True
    return False

def solve():
    t = int(raw_input())
    for k in range(1, t+1):
        vals = raw_input().split(" ");
        n = int(vals[0])
        m = int(vals[1])

        master = []
        for i in range(0, n):
            d = raw_input()
            li = d.split("/")
            cur = ""
            for x in li:
                if(x == ""):
                    continue;
                cur += "/" + x
                if(not find(cur, master)):
                    # print cur
                    master.append(cur)

        ans = 0
        for i in range(0, m):
            d = raw_input()
            li = d.split("/")
            cur = ""
            for x in li:
                if(x == ""):
                    continue;
                cur += "/" + x
                if(not find(cur, master)):
                    ans += 1
                    # print "ani " + cur
                    master.append(cur)

        print "Case #" + str(k) + ": " + str(ans)
if __name__ == "__main__":
    solve()

