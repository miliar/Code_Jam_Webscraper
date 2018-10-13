def answer(dist, horses):
    times = [(dist-h[0])/h[1] for h in horses]

    # for i in range(1, len(horses)):
    #     if (times[i-1] > times[i]):
    #         d = horses[i-1][0] - horses[i][0]
    #         ti = d / (horses[i-1][1] - horses[i][1])
    #         times[i] = ti + (horses[i-1][0])

    return dist / max(times)

def case_print(case, result):
    print("Case #" + str(case) + ":", result)

if __name__ == "__main__":
    for c in range(int(input())):
        dist, n = map(int, input().split())
        horses = []
        for h in range(n):
            horses.append(tuple(map(int, input().split())))
        case_print(c + 1, answer(dist, horses))
