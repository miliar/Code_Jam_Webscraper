def solve(n):
    for i in range(n, 0, -1):
        s = str(i)
        if s == "".join(sorted(s)):
            return s
    return "ERROR"

if __name__=="__main__":
    line_count = int(input())
    for i in range(1, line_count + 1):
        n = int(input())
        result = solve(n)
        print("Case #{}:".format(i), result)
