num_tests = int(input())
for test in range(1, num_tests + 1):
    line = input().split(' ')
    distance = int(line[0])
    n_horses = int(line[1])
    horses = []
    for horse in range(n_horses):
        line = input().split(' ')
        horses.append((int(line[0]), int(line[1])))
    finish_times = []
    for pos, speed in horses:
        finish_times.append((distance - pos) / speed)
    slowest_time = max(finish_times)
    avg_speed = distance / slowest_time
    print('Case #{}: {}'.format(test, avg_speed))
