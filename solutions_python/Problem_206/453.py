debug = False

def dbg_print(x):
    if debug:
        print(x)


def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        d, n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        maxt = -1
        for j in range (1, n + 1):
            k, s = [int(s) for s in input().split(" ")]
            t = 1. * (d - k) / s
            dbg_print("k:{} s:{} t:{} maxt:{}".format(k,s,t,maxt))
            if maxt == -1 or t > maxt:
                maxt = t
                maxk = k
                maxs = s

        speed = 1. * d / maxt

        print("Case #{}: {:f}".format(i, speed))

if __name__ == "__main__":
    main()
