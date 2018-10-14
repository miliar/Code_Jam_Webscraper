def calc_rides(line1, line2):
    rides, capacity, num_groups = int(line1[0]), int(line1[1]), int(line1[2])
    groups = [int(i) for i in line2]
    money = 0
    count = 0
    #print(rides, capacity, num_groups)
    while count < rides:
        #print(count, 'of', rides)
        r = 0
        tmp = []
        while len(groups) > 0 and (r + groups[0]) <= capacity:
            #print(r, tmp, groups)
            g = groups.pop(0)
            r += g
            tmp.append(g)
        money += r
        groups.extend(tmp)
        count += 1
        
    return money

def split(line):
    return line.replace('\n', '').split(' ')

if __name__ == '__main__':
    
    input_problem = 'C'
    input_set = 'small-attempt0'
    in_file = open('{}-{}.in'.format(input_problem, input_set), 'r')
    out_file = open('{}-{}.out'.format(input_problem, input_set), 'w')

    line = in_file.readline()

    count = int(line)
    for i in range(1, count+1):
        line1 = split(in_file.readline())
        line2 = split(in_file.readline())
        out_file.write('Case #{}: {}\n'.format(i, calc_rides(line1, line2)))

    in_file.close()
    out_file.close()

