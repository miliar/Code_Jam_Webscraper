
def main():
    case = int(input())
    for n in range(case):
        opt = [int(r) for r in (input().split(" "))]
        a, b, k = opt[0], opt[1], opt[2]
        c = []
        for i in range(a):
            for j in range(b):
                temp = i&j
                if temp < k:
                    c.append(i&j)
        header = "Case #" + str(n+1) + ":"
        print(header, len(c))
if __name__ == '__main__':
    main()

