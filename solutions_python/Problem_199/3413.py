
import sys




def switcher(string , num):
    final_string = ''

    if len(string) < num:
        return False
    for element in string:
        if element == '-' and num > 0:
            final_string = final_string + '+'
        elif element == '+' and num > 0:
            final_string = final_string + '-'
        else:
            final_string = final_string + element
        num = num -1

    print(final_string)
    return final_string

def plus_detonation(string):
    return_string = string
    print (string)
    for element in string:
        if element == '+':
            string = string [1:]
            print (string)
            return_string = string
        elif element == '-':

            return return_string
            break

    return return_string
print (plus_detonation('+---'))

def solver(string, num):
    temp_string = string
    print (string)
    temp_string = plus_detonation(temp_string)
    counter = 0
    print (temp_string)
    if temp_string == '':
        return counter
    while temp_string != '':

        temp_string = switcher(temp_string, num)
        counter += 1
        if  temp_string == False:
            return 'IMPOSSIBLE'
            break

        else:
            temp_string = plus_detonation(temp_string)

    return counter


input_file = sys.argv[1] + '.in'
output_file = sys.argv[1] + '.out'
def inputer(input_file):
    output_list = []
    with open (input_file) as fin:
        finx = fin.read().split('\n')
        biglist = [line.strip().split(' ') for line in finx]
        biglist = biglist[1:-1]
    return biglist

biglist = inputer(input_file)
return_list = []
for element in biglist:
    test_string = element[0]
    test_num = int(element[1])

    return_list.append(solver(test_string, test_num))


def outputer(output_file, return_list):
    with open (output_file, 'w') as out:
        x = 1
        for element in return_list:
            if element == 'IMPOSSIBLE':
                out.write('Case #%d: %s \n' %(x, element))
            else:
                out.write('Case #%d: %d \n' %(x, element))
            x += 1
outputer(output_file, return_list)
