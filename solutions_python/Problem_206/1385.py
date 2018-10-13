T = int(input())
for t in range(T):
    D, N = input().split()
    D, N = [int(D), int(N)]
    traj = []
    time = []
    for i in range(N):
        Ki, Si = input().split()
        traj.append((int(Ki), int(Si)))
        time.append((D - traj[i][0]) / traj[i][1])
    tMax = max(time)
    print("Case #" + str(t + 1) + ": " + str(D/tMax))
