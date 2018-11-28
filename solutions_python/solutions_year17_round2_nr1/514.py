#--- READ INPUT ---#
#inp = open('A-small-attempt0.in', 'r')
inp = open('A-large.in', 'r')
#inp = open('test.in', 'r')
o = open('output_large.txt', 'w')

test_cases = int(inp.readline())
for i in range(test_cases):
    line = inp.readline()[:-1].split(' ')
    d = int(line[0])
    n = int(line[1])
    max_time = 0
    for j in range(n):
        line = inp.readline()[:-1].split(' ')
        km = int(line[0])
        speed = int(line[1])
        time = (d - km) / speed
        max_time = max_time if max_time > time else time

    final_speed = d / max_time

    #--- WRITE OUTPUT ---#
    s = 'Case #' + str(i+1) + ': ' + str(final_speed)
    o.write(s + '\n')
inp.close()
o.close()
