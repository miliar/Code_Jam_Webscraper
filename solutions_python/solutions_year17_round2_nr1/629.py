def manager(dest,num,horses):
    time = []
    for horse in horses:
        distance = dest - int(horse[0])
        time.append( distance / int(horse[1]))
    result =dest/max(time)
    return result

t = int(input())
for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]
    horses = []
    for ni in range(n):
        horses.append(input().split(" "))
    result = manager(d,n,horses)
    print("Case #{}: {}".format(i, result))
