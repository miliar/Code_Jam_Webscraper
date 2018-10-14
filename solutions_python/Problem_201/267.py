import sys

def parse(line):
    i = 0
    while not line[i] == ' ':
        i += 1
    n = int(line[:i])
    k = int(line[i:])
    
    return [n, k]

def get_next_values(current):
    next_values = []
    for i in current:
        if i <= 1:
            continue
        if i % 2 == 0:
            if not i/2 in next_values:
                next_values.append(i/2)
            if not (i/2-1) in next_values:
                next_values.append(i/2-1)
        else:
            if not (i-1)/2 in next_values:
                next_values.append((i-1)/2)
    return next_values

            
def get_next_level(current):
    current_values = []
    next_level = {}
    for diff in current:
        current_values.append(diff[0])
    for value in get_next_values(current_values):
        next_level[value] = 0
    if len(next_level) == 0:
        return -1
    for diff in current:
        val = diff[0]
        num = diff[1]
        if val % 2 == 0:
            next_level[val/2] += num
            next_level[val/2-1] += num
        else:
            next_level[(val-1)/2] += 2*num
    to_return = []
    for key, value in next_level.iteritems():
        to_return.append([key, value])
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(to_return)-1):
            if to_return[i][0] < to_return[i+1][0]:
                temp = to_return[i]
                to_return[i] = to_return[i+1]
                to_return[i+1] = temp
                is_sorted = False
    return to_return

    
def get_levels(n):
    levels = []
    current_level = [[n,1]]
    levels.extend(current_level)
    next_level = get_next_level(current_level)
    while next_level != -1:
        levels.extend(next_level)
        next_level = get_next_level(next_level)
    return levels

def get_min_max(n,k):
    levels = get_levels(n)
    current_level = -1
    while k > 0:
        current_level += 1
        k -= levels[current_level][1]
    result = levels[current_level][0]
    maxi = 0
    mini = 0
    if result %2 == 1:
        maxi = (result-1)/2
        mini = (result-1)/2
    else:
        maxi = result/2
        mini = result/2 - 1
    return [mini, maxi]


#returns string    
def solution(line):
    to_pass = parse(line)
    ans = get_min_max(to_pass[0],to_pass[1])
    return str(ans[1])+' '+str(ans[0])

    
in_file = sys.argv[1]
in_stream = open(in_file)
lines = in_stream.readlines()

for i in range(1,len(lines)):
    print 'Case #%d: '%i +solution(lines[i])
