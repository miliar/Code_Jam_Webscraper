



def time(x, counter, step):
    return float(x - counter) / step

input = open('input.txt', 'r')
output = open('output.txt', 'w')

num_of_test = int(input.readline().rstrip())

for i in range(1, num_of_test+1):
    line = input.readline().rstrip().split(' ')
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    
    counter = 0
    step = 2
    res = 0
    if x < c:
        res = x / step
        counter = x
    while (counter < x):
        if counter < c:
            res += float(c - counter) / step
            counter = c
        else:
            if time(x, counter, step) < time(x, counter - c, step + f):
                res += time(x, counter, step)
                counter = x
            else:
                counter -= c
                step += f
    output.write('Case #%d: %.7f\n' %(i, res))

