# import here


def solve(cake):
    for rnum, r in enumerate(cake):
        pen = '?'
        for i in range(0, len(r)):
            if r[i] == '?':
                r = r[:i] + pen + (r[i+1:] if i+1 < len(r) else '')
            else:
                pen = r[i]
            # print(pen, r, i)

        pen = '?'
        for i in range(len(r)-1, -1, -1):
            if r[i] == '?':
                r = r[:i] + pen + (r[i+1:] if i+1 < len(r) else '')
            else:
                pen = r[i]
            # print(pen, r, i)

        cake[rnum] = r

    pen = "?" * len(cake[0])
    for i in range(0, len(cake)):
        if cake[i] == "?" * len(cake[i]):
            cake[i] = pen
        else:
            pen = cake[i]
        # print(i, cake[i])

    pen = "?" * len(cake[0])
    for i in range(len(cake)-1, -1, -1):
        if cake[i] == "?" * len(cake[i]):
            cake[i] = pen
        else:
            pen = cake[i]
        # print(i, cake[i])


def main():
    T = int(input())

    for casenum in range(1, T+1):
        # n = int(input())
        r, c = [int(s) for s in input().split(" ")]
        # s = input()

        cake = []
        for i in range(r):
            cake.append(input())

        solve(cake)

        print("Case #{}:".format(casenum))

        for r in cake:
            print(r)

if __name__ == "__main__": main()
