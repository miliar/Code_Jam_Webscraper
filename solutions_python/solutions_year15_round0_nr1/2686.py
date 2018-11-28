def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            raw_data = f.readline().strip()
            max_shyness,audience = raw_data.split(' ')
            data.append([int(max_shyness),[int(val) for val in audience]])
        return data
            


def solve_ovation(data):
    case = 1
    for element in data:
        audience = element[1]
        ovation = 0
        needed = 0
        for shyness in range(len(audience)):
            if shyness <= ovation:
                ovation += audience[shyness]
            else:
                needed += shyness - ovation
                ovation += (shyness - ovation) + audience[shyness]

        
        print "Case #{}: {}".format(case,needed)
        case += 1

solve_ovation(read_data('A-large.in'))
