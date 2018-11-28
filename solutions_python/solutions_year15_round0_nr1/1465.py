try:
    raw_input = raw_input
except:
    raw_input = input

def standing_ovation(s_max, shyness_list):
    needed_people = 0

    stood_up = [False] * (s_max + 1)
    sum_stood = [0] * (s_max + 1)

    stood_up[0] = True if shyness_list[0] else False
    sum_stood[0] = shyness_list[0] if stood_up[0] else 0

    # Optimization hint execution
    if not stood_up[0]:
        stood_up[0] = True
        sum_stood[0] = 1
        needed_people += 1

    for index, shyness_number in enumerate(shyness_list):
        if index == 0:
            continue

        if stood_up[index - 1] and sum_stood[index - 1] >= index:
            stood_up[index] = True
            sum_stood[index] = sum_stood[index - 1] + shyness_number
        else:
            if stood_up[index - 1]:
                people_for_the_next_level = index - sum_stood[index - 1]
                needed_people += people_for_the_next_level
                sum_stood[index] = sum_stood[index - 1] + people_for_the_next_level + shyness_number
                stood_up[index] = True
            else:
                print ('[HINT] Optimization around stood_up[0] may be needed. (State: S_{index})'.format(index=index))

    return needed_people

def main():
    T = int(raw_input())
    for t_i in range(T):
        max_shyness, shyness_str = raw_input().split(' ')

        max_shyness = int(max_shyness)
        shyness_str = map(int, list(shyness_str))

        print ('Case #{t_i}: {answer}'.format(t_i=t_i+1, answer=standing_ovation(max_shyness, shyness_str)))

if __name__ == '__main__':
    main()
