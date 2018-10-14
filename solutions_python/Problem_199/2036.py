def check_cakes(cakes):
    for i in range(len(cakes)):
        if cakes[i] == '-':
            return i
    return -1


def solve_case(info):
    splits = info.split(' ')
    size = eval(splits[1])
    cakes_string = splits[0]

    cakes  = []
    for c in cakes_string:
        cakes.append(c)

    flip_count = 0
    cake_status = check_cakes(cakes)
    while cake_status != -1 and cake_status <= (len(cakes) - size):
        flip_count += 1
        #print (cakes)
        for i in range(cake_status, cake_status + size):
            if cakes[i] == '+':
                cakes[i] = '-'
            else:
                cakes[i] = '+'
        cake_status = check_cakes(cakes)

    if cake_status >= (len(cakes) - size):
        return -1
    else:
        return flip_count

with open('q1_input.txt', 'r') as f:
    lines = f.readlines()
    num_cases = eval(lines[0])

    #cases = []
    for i in range(1, len(lines)):
        #cases.append(lines)
        #print ('Solving ---' + str(i) )
        status = solve_case(lines[i])
        if status == -1:
            print ('Case #' + str(i) + ': ' + 'IMPOSSIBLE')
        else:
            print ('Case #' + str(i) + ': ' + str(status))
