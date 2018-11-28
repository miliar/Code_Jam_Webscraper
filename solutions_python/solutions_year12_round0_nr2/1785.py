import sys

def solve(s, p, points_list):
    num = 0
    for points in points_list:
        maxpoints = points // 3 + (0 if points % 3 == 0 else 1)
        if maxpoints >= p:
            num+=1
        else:
            if maxpoints + 1 >= p and s > 0 and points > 0:
                s-=1
                num+=1
    return num


def main():
    sys.stdin.readline()
    i = 1
    for line in sys.stdin:
        inp = [int(x) for x in line.strip().split(' ')]
        print("Case #" + str(i) + ": " + str(solve(inp[1], inp[2], inp[3:])))
        i+=1

main()
