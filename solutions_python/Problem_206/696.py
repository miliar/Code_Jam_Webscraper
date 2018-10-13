def solve(D, N, pos, speed):
    slowest = float("inf")

    for j in range(N):
        sp = float(D - pos[j])/float(speed[j])
        ti = float(D/sp)
        if ti < slowest:
            slowest = ti

    return slowest

if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        N_line = input().split(" ")
        D = int(N_line[0])
        N = int(N_line[1])

        pos = list()
        speed = list()

        for i in range(N):
            li = input().split(" ")
            pos.append(float(li[0]))
            speed.append(float(li[1]))

        print("Case #%i: %s" % (nth_case, solve(D, N, pos, speed)))
