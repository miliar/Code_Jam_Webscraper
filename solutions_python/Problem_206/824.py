for i in range(int(input())):
    d, n = input().split()
    d = int(d)
    n = int(n)
    horse_time = []
    for j in range(n):
        k, s = input().split()
        k = int(k)
        s = int(s)
        difference = (d - k) / s
        horse_time.append(difference)
    max_time = max(horse_time)
    speed = d / max_time
    print("Case #"+ str(i+1)+ ":",speed)
