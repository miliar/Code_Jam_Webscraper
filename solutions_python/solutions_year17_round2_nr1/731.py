def solution(d, n, k, s):
    horses = []
    for i in range(n):
        horses.append((k[i], s[i]))
    horses.sort(key=lambda x: x[0])
    current_speed = d / ((d - horses[0][0]) / horses[0][1])
    for i in range(1, len(horses)):
        if current_speed > horses[i][1]:
            t = horses[i][0] / (current_speed - horses[i][1])
            if t * current_speed < d:
                total = t + (d - t * current_speed) / horses[i][1]
                current_speed = d / total

    return current_speed

t = int(input())

for i in range(t):
    d, n = map(int, input().split())
    k = []
    s = []
    for _ in range(n):
        k_i, s_i = map(int, input().split())
        k.append(k_i)
        s.append(s_i)
    print("Case #%d: %.7f" % (i+1, solution(d, n, k, s)))
