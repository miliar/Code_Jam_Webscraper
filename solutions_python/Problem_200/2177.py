def borrow(number, pos):
    #if number[pos] != 0:
    #    print ('Cant borrow at pos=' + str(pos))
    #    return number

    number[pos] = 9
    number[pos - 1] -= 1

    if pos - 1 == 0 or number[pos - 2] <= number[pos - 1]:
        return number
    else:
        return borrow(number, pos - 1)

def clean_up(number):
    result  = []
    #print ('Cleaning up' + str(number))
    fill_9 = False
    beginning = True
    for n in number:

        if beginning:
            if n != 0:
                beginning = False
        if not beginning:
            if n == 9:
                fill_9 = True

            if fill_9 == True:
                result.append(9)
            else:
                result.append(n)

    return result


def find_tidy(info):
    number = []
    #print (info)
    for n in info:
        number.append(eval(n))

    prev = -1
    result = number
    for i in range(len(number)):
        if number[i] < prev:
            result = borrow(number, i)
            break
        #######################################
        prev = number[i]
    return clean_up(result)


with open('q2_input.txt', 'r') as f:
    lines = f.readlines()

    num_cases = eval(lines[0])

    for i in range(1, len(lines)):
        number = find_tidy(lines[i].strip())

        good_stuff = ''
        for n in number:
            good_stuff += str(n)

        print ('Case #' + str(i) + ': '  + good_stuff)
