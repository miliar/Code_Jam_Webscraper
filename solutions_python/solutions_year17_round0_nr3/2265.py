import math
def read_line():
    file = open('input.file', 'r')
    dict = {
        'count': 0,
        'cases' : []
    }
    dict['count'] = int(file.readline())
    lines = file.readlines()
    for i in range(len(lines)):
        lst = lines[i].replace('\n', '').split(' ')

        dict['cases'].append({
            'N' : int(lst[0]),
            'K' : int(lst[1]),
        })
    return dict

'''
    n stalls count,  k is # of persons
'''

def calc_state(n,k):
    state_dict = {
        'min': 0,
        'max': 0,
    }

    stalls = {}
    stalls[n] = 1
    duplicate = 0

    if n == k:
        return {
            'max': 0,
            'min': 0,
        }

    i = 0


    while i < k:
        current = max(stalls.keys())
        num = current // 2
        state_dict['min'] = num-1 if current % 2 == 0 else num
        state_dict['max'] = num

        if stalls[current] == 1 and duplicate == 0:
            update_val(stalls, state_dict,1)
        elif duplicate == 0:
            val = stalls[current]
            update_val(stalls, state_dict, val)
            duplicate = stalls[current]

        stalls.pop(current)

        i += duplicate + 0 if duplicate > 0 else 1
        duplicate = 0

    return state_dict




def update_val(stalls, state_dict, val):
    stalls[state_dict['max']] = stalls[state_dict['max']] + val if state_dict['max'] in stalls else val
    stalls[state_dict['min']] = stalls[state_dict['min']] + val if state_dict['min'] in stalls else val





def main():
    test = read_line()
    file = open('output.file', 'w')
    for i in range(test['count']):
        case = test['cases'][i]
        n = case['N']
        k = case['K']
        result = calc_state(n,k)
        file.write("Case #{0}: {1} {2}\n".format(i+1, result['max'], result['min']))
    file.close()
if __name__ == '__main__':
    main()