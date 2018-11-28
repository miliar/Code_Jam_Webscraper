lines = open('data.txt').read()
output = open('output.txt', 'w')

lines = lines.splitlines()
cases_num = int(lines[0])
lines = lines[1:]
cur_index = 0


def get_absorbed(other_motes, mote_size):
    rest_motes = []
    for o_mote in other_motes:
        if o_mote < mote_size:
            mote_size += o_mote
        else:
            rest_motes.append(o_mote)
    return mote_size, rest_motes

for i in range(cases_num):
    case_num = i + 1
    a, n = lines[cur_index].split()
    mote_size = int(a)
    cur_index += 1
    other_motes = sorted([int(x) for x in lines[cur_index].split()])
    # absorb all possible other motes
    mote_size, rest_motes = get_absorbed(other_motes, mote_size)
    opt_number = len(rest_motes)

    if mote_size > 1 and opt_number > 0:
        new_opt_numbers = []
        # now try to add less number
        for i in range(opt_number):
            temp_number = i + 1
            mote_size += mote_size - 1
            _, new_rest_motes = get_absorbed(rest_motes, mote_size)
            new_opt_numbers.append(temp_number+len(new_rest_motes))

        opt_number = min([opt_number, min(new_opt_numbers)])
    cur_index += 1

    output.write('Case #{0}: {1}'.format(case_num, opt_number) + '\n')
    print 'Case #{0}: {1}'.format(case_num, opt_number)


