def check_keys(keys, chests):
    required_keys = []
    available_keys = keys[:]
    for chest in chests:
        required_keys.append(chest[0])
        for i in range(chest[1]):
            available_keys.append(chest[2+i])

    all_keys_present = True

    try:
        for x in required_keys:
            available_keys.remove(x)
    except ValueError:
        all_keys_present = False

    return all_keys_present


def check_chests(keys, remaining_chests):
    required_keys = []
    available_keys = keys[:]
    for chest in remaining_chests:
        required_keys.append(chest[0])
        for i in range(chest[1]):
            elem = chest[2+i]
            if elem != chest[0]:
                available_keys.append(elem)

    available_keys = list(set(available_keys))
    required_keys = list(set(required_keys))

    '''
    print('required : ',required_keys)
    print(remaining_chests)
    print('availabe : ',available_keys)
    '''

    all_keys_present = True

    try:
        for x in required_keys:
            available_keys.remove(x)
    except ValueError:
        all_keys_present = False

    return all_keys_present

    

def solve(keys, chests, remaining_chests, solution):
    completed = True
    for i in range(len(chests)):
        if i+1 not in solution:
            completed = False
            break
    if completed:
        return True
    elif keys == []:
        return False

    for i, chest in enumerate(chests):
        if (i+1 not in solution) and (chest[0] in keys):
            #print(keys,solution)
            solution.append(i+1)
            keys.remove(chest[0])
            for j in range(chest[1]):
                keys.append(chest[2+j])
            remaining_chests.remove(chest)
            if (check_chests(keys,remaining_chests) == False) or (solve(keys,chests,remaining_chests, solution) == False):
                #print(keys,solution)
                keys.append(chest[0])
                for j in range(chest[1]):
                    keys.remove(chest[2+j])
                solution.remove(i+1)
                remaining_chests.append(chest)
            else:
                return True
    return False


f = open('D-small-attempt2.in', 'r')

output = open('output.txt','w')

T = int(f.readline())

for i in range(1,T+1):
    line1 = (f.readline().rstrip()).split(' ')

    num_of_keys = int(line1[0])
    num_of_chests = int(line1[1])

    keys = [int(x) for x in (f.readline().rstrip()).split(' ')]

    #print(line1)

    chests = []
    solution = []

    for j in range(num_of_chests):
        chests.append([int(x) for x in (f.readline().rstrip()).split(' ')])

    remaining_chests = chests[:]

    if num_of_keys > 0 and check_keys(keys,chests):
        solve(keys, chests, remaining_chests, solution)

    if solution != []:
        result = ' '.join([str(x) for x in solution])
    else:
        result = "IMPOSSIBLE"

    text = 'Case #'+str(i)+': '+result

    print(text,file=output)
    #print(text)

f.close()
output.close()

#print(lines)
