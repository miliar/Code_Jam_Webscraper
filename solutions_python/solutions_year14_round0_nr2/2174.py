#%%
file_ = open('input')
output_file = open('output', 'w')

test_cases = int(file_.readline())

#%%
for test_case in range(test_cases):
    output_file.write('Case #{}: '.format(test_case + 1))
    c, f, x = [float(item) for item in file_.readline().split()]

    time = 0.0
    rate = 2.0
    while (c / rate) + (x / (rate + f)) < x / rate:
        time += c / rate
        rate += f
    time += x / rate
    output_file.write('{:.7f}\n'.format(time))