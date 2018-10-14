t = int(raw_input().strip())
for i in range(t):
    d, n = map(int , raw_input().strip().split(' '))
    time_taken = []
    for j in range(n):
        k, s = map(int, raw_input().strip().split(' '))
        time = round((d - k) / float(s), 6)
        time_taken.append(time)
    max_time = max(time_taken)
    max_speed = round(d / max_time, 6)
    print 'Case #{0}: '.format(i+1) + format(max_speed, '.6f')
