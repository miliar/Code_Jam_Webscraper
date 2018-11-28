def solve(D, N, horses):
    i = 0
    times = [0.0 for j in horses]
    while i < len(horses):
        next = i + 1
        time_actual = (D - horses[i][0]) / horses[i][1]
        if next == len(horses):
            times[i] = time_actual
            break
        
        time_next = (D - horses[next][0]) / horses[next][1]
        while next < len(horses) and time_actual >= time_next:
            time_next = (D - horses[next][0]) / horses[next][1]
            next += 1
            
        if next == len(horses):
            times[i] = time_actual
        else:
            times[i] = time_next

        i = next
    return D / max(times)


T  = int(input().strip())
for i in range(T):
    D, N = [int(z) for z in input().strip().split(" ")]
    horses = []
    for j in range(N):
        Kj, Sj = [int(z) for z in input().strip().split(" ")]
        horses.append((Kj, Sj))
    sol = solve(D,N, horses)
    print("Case #" + str(i + 1) + ":", sol)
