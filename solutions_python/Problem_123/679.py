def count_of_add(my_mote, target_mote):
    counter = 0
    while my_mote <= target_mote:
        my_mote += my_mote - 1
        counter += 1
    return my_mote, counter


def add_up_to_mote(my_mote, target_mote, counter):
    m, c = count_of_add(my_mote, target_mote)
    return m, counter + c


def remove_mote(counter):
    return counter + 1


def solve_case(case):
    my_mote = case['my_mote']
    counter = 0
    for i, mote in enumerate(case['motes']):
        if my_mote > mote:
            my_mote += mote
        elif my_mote <= 1:
            counter = remove_mote(counter)
        elif i == len(case['motes']) - 1:
            counter = remove_mote(counter)
        elif count_of_add(my_mote, mote)[1] < len(case['motes']) - i:
            my_mote, counter = add_up_to_mote(my_mote, mote, counter)
            my_mote += mote
        else:
            counter = remove_mote(counter)
    return counter

#input_file = "input.txt"
input_file = "/Users/gerrrr/Downloads/A-small-attempt5.in"

cases = []
with open(input_file) as f:
    f.readline()
    text = f.read().strip().split('\n')
    while text:
        my_mote, _ = map(int, text.pop(0).split())
        motes = sorted(map(int, text.pop(0).split()))
        cases.append({'my_mote': my_mote, 'motes': motes})

#print cases[16], solve_case(cases[16])

#for i, x in enumerate(cases):
#    print i + 1, x, len(x['motes']), solve_case(x)

for i, r in enumerate(map(solve_case, cases)):
    print 'Case #%s: %s' % (i + 1, r)
