def read_file(file_name):
    f = open(file_name, 'r')
    first_line = f.readline()
    return_str = ""
    for i in range(0, int(first_line)):
        number = f.readline().split(' ')
        answer = get_minimum_flips(number[0], int(number[1]))
        return_str += 'Case #'+str(i+1)+': '+str(answer)
        return_str += '\n'

    return return_str

def get_minimum_flips(pancake_order, k):
    number_of_flips = 0
    for i in range(0, len(pancake_order)):
        if pancake_order[i] == '-':
            pancake_order = flip_pancakes(pancake_order,i,k)
            if pancake_order == "":
                return "IMPOSSIBLE"
            else:
                number_of_flips = number_of_flips + 1
    return number_of_flips

def flip_pancakes(pancake_order, i, k):
    if i + k > len(pancake_order):
        return ""
    x = list(pancake_order)
    for j in range(0,k):
        if x[j + i] == '-':
            x[j + i] = '+'
        else:
            x[j + i] = '-'
    return ''.join(x)


output = read_file('A-large.in')
output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()