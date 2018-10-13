T = int(raw_input())

for case in range(1, T+1):
    D, N = map(int, raw_input().strip().split())
    horses = []
    for horse in range(N):
        horses.append(map(int, raw_input().strip().split())) # K , S

    max_reaching_time = 0
    for horse in horses:

        K , S = horse
        t = (D-K) / float(S)
        max_reaching_time = max(max_reaching_time, t)


    print("Case #{}: ".format(case)+"%.6f" % (D / max_reaching_time))