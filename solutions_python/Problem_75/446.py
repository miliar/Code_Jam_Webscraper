reader = open('B-large.in')
writer = open('output-B-large', 'w')

test_cases = int(reader.readline())

for kount in range(test_cases):
    line = reader.readline().split(' ')

    combines = []
    opposed = []

    idx = 0

    # read combined
    if line[idx] == '0':
        idx += 1
    else:
        n_combines = int(line[idx])
        idx += 1
        for k in range(n_combines):
            combines.append(line[idx])
            idx += 1

    # read opposed
    if line[idx] == '0':
        idx += 1
    else:
        n_opposed = int(line[idx])
        idx += 1
        for k in range(n_opposed):
            opposed.append(line[idx])
            idx += 1

    # we don't need the length, but whatever
    chars = int(line[idx])
    idx += 1

    seq = line[idx][:-1]
    elem_list = []
    for item in seq:
        elem_list.append(item)
        # check if the last two combine
        flag = False
        if len(elem_list) > 1:
            c = elem_list[-1] + elem_list[-2]
            for g in combines:
                if g[:2] == c or g[:2][::-1] == c:
                    elem_list = elem_list[:-2] + list(g[-1])
                    flag = True

        # check if something in the list is opposed
        if not flag:
            for o in opposed:
                if item == o[0]:
                    if o[1] in elem_list:
                        elem_list = []
                elif item == o[1]:
                    if o[0] in elem_list:
                        elem_list = []

    clean = '[' + ', '.join(elem_list) + ']'
    writer.write('Case #%s: %s' % (str(kount + 1), clean) + '\n')

reader.close()
writer.close()
    
