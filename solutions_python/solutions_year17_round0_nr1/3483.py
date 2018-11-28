
def flip_pancake(pancake):
    if pancake == '-':
        return '+'
    else:
        return '-'

def flip_pancakes(case_number, pancakes, k, f):
    count = 0
    answer = ""

    while '-' in pancakes:
        pancakes_list = list(pancakes)
        first_occurence_of_negative_pancake_to_be_flipped = pancakes.find('-')

        if first_occurence_of_negative_pancake_to_be_flipped == -1:
            break

        if (first_occurence_of_negative_pancake_to_be_flipped + k - 1 > len(pancakes) - 1):
            answer = 'Case #{}: IMPOSSIBLE'.format(case_number)
            break

        for i in range(first_occurence_of_negative_pancake_to_be_flipped,
                       first_occurence_of_negative_pancake_to_be_flipped + k):
            pancakes_list[i] = flip_pancake(pancakes_list[i])
        count += 1

        pancakes = "".join(pancakes_list)

    if answer != 'Case #{}: IMPOSSIBLE'.format(case_number):
        answer = 'Case #{}: {}'.format(case_number, count)

    print(answer)
    f.write(answer + '\n')

if __name__ == '__main__':
    lines = [line.strip('\n') for line in open('./A-large.in')]
    f = open('A-large.out', 'w')

    i = 1
    for line in lines[1:]:
        params = line.split(" ")
        pancakes = params[0]
        k = int(params[1])
        flip_pancakes(i, pancakes, k, f)
        i += 1

    f.close()  # you can omit in most cases as the destructor will call it