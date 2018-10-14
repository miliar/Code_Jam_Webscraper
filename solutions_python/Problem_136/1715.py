input = open('B-small-attempt1.in', 'r')
output = open('B-small-attempt1.out', 'w')

test_count = input.readline()

for i in range(0, int(test_count)):
    line = input.readline().rstrip().split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    needed_time = 0.0
    needed_time_min = float('inf')
    j = -1
    while True:
        j += 1
        speed = 2.0
        factory_time = 0.0
        for k in range(0, j):
            factory_time += c / speed
            speed += f
        needed_time = x / speed + factory_time
        if needed_time < needed_time_min:
            needed_time_min = needed_time
        else:
            break
    print needed_time_min
    output.write("Case #" + str(i + 1) + ": " + str(needed_time_min) + "\n")

input.close()
output.close()
