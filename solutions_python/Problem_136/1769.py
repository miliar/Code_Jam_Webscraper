from __future__ import print_function

input_file = open('input.txt')
output_file = open('output.txt', 'w')

count = int(input_file.readline())

for i in range(count):
    c, f, x = map(float, input_file.readline().split())

    best_time = x / 2
    j = 0
    while True:
        time = 0
        for k in range(j + 1):
            time += c / (2 + k * f)
        time += x / (2 + (j + 1) * f)

        if time < best_time:
            best_time = time
        elif j > 0 and time >= best_time:
            break

        j += 1
    case = 'Case #{0}:'.format(i + 1)
    print(case, best_time, file=output_file)
output_file.close()
