f = open('A-large.in', 'r')
# f = open('input.txt' , 'r')
n = int(f.readline())
f_out = open('output.txt', 'w')

for test_idx in range(1, n+1):
    row = f.readline().split()
    s_max = int(row[0])
    needed = 0
    running_sum = 0
    for val in range(0, s_max+1):
        count = int(row[1][val])
        if val > running_sum:
            needed += val - running_sum
            running_sum = val
        running_sum += count

    f_out.write('Case #' + str(test_idx) + ': ' + str(needed) + '\n')
