import math

inp = open("in.txt", 'r')
out = open("out.txt", 'w')
num_case = 0

for line in inp:
    if num_case is 0:
        num_case += 1
        continue
    line_list = line.split()
    rooms = int(line_list[0])
    people = int(line_list[1])
    rooms_list = [(0, rooms-1)]
    '''
    i = 0
    while math.pow(2,i) < people:
        i += 1
    i -= 1
    diff = people - math.pow(2,i)
    '''
    bin_people_str = bin(people)[2:]
    bin_people = list(bin_people_str)
    bin_people.reverse()
    next_block = rooms
    r = 0
    l = 0
    for j in range(len(bin_people)):
        r = math.ceil(float(next_block-1)/2)
        l = math.floor(float(next_block-1)/2)
        if bin_people[j] == '1':
            next_block = l
        if bin_people[j] == '0':
            next_block = r

    out.write("Case #" + str(num_case) + ": "+str(r) + ' '+ str(l)+"\n")
    num_case += 1

out.close()
inp.close()