def tom_cruise(horses, dest):
    # Find out which horse takes the longest
    mx = float('-inf')
    for horse in  horses:
        k, s = horse
        time = (dest-k)/s
        mx = max(mx, time)
    return dest/mx

T = int(input())
for t in range(1, T+1):
    dest, n = map(int, input().split(' '))
    horses = []
    for i in range(n):
        k, s = map(int, input().split(' '))
        horses.append((k, s))
    cruise = tom_cruise(horses, dest)
    print('Case #', t, ': ', cruise, sep='')
