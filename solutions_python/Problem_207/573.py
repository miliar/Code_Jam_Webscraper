
colors = ["R", "O", "Y", "G", "B", "V"]


def solvesmall(line):
    return greedy(line[0], line[1:])


def greedy(n, counts):
    l = []
    for i in range(n):
        m = 0
        for j in range(6):
            if(l == [] or j != l[-1]) and (counts[j] > m or (l !=[] and counts[j] == m and m >0 and j == l[0])):
                m = counts[j]
                c = j
        if m == 0:
            return "IMPOSSIBLE"
        l += [c]
        counts[c] -= 1
    if l[-1] == l[-2] or l[-1] == l[0]:
        return "IMPOSSIBLE"
    else:
        return "".join([colors[c] for c in l])


def DFS(n, counts):

    l = []
    # print n, counts

    def forward(i, j):
        l.append(j)
        counts[j] -= 1
        return i+1, 0

    def backward(i):
        j = l.pop()
        counts[j] += 1
        return i-1, j + 1

    i = 0
    c = 0

    while(i < n):
        print l
        # print l, counts, i, c
        if i == 0:
            for j in range(c, 6):
                if counts[j] != 0:
                    i, c = forward(0, j)
                    break
            else:
                return "IMPOSSIBLE"
        elif i == n - 1:
            for j in range(0, 6):
                if counts[j] != 0 and j != l[-1] and j != l[0]:
                    return "".join([colors[c] for c in l + [j]])
            else:
                i, c = backward(i)
        else:
            for j in range(1, 6):
                if counts[j] > ((n - i) / 2) + 1:
                    i, c = backward(i)
                    break

            for j in range(c, 6):
                if counts[j] != 0 and j != l[-1]:
                    i, c = forward(i, j)
                    break
            else:
                i, c = backward(i)




def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        line = [int(s) for s in raw_input().split(" ")]
        sol = solvesmall(line)
        print "Case #{}: {}".format(i, sol)


if __name__ == "__main__":
    main()
