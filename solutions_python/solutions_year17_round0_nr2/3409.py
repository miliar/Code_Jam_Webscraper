from sys import stdin
def solve(s):
    s=list(map(int,s))
    orden=list(map(int,s))
    orden.sort()
    if s==orden:
        return "".join(list(map(str,s)))
    else:
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                x=len(s)
                s[i]-=1
                del s[i+1:]
                s=s+[9]*(x-i-1)
                if s[0]==0:
                    del s[0]
                return solve("".join(list(map(str,s))))
def main():
    n=int(stdin.readline())
    for i in range(n):
        s=stdin.readline().strip()
        print("Case #"+str(i+1)+": "+solve(s))
main()
