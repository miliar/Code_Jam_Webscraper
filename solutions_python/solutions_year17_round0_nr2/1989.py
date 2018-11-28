

def is_ascending(num):
    return sorted(num) == num


def calc(number):
    number = list(number)
    if is_ascending(number):
        return "".join(number)
    for ind in range(len(number)-1, -1, -1):
        dig = int(number[ind])
        while dig > 0:
            number[ind] = str(dig-1)
            if is_ascending(number):
                return "".join(number)
            else:
                dig -= 1
        if dig == 0:
            number[ind] = '9'


for i in range(input()):
    output = calc(raw_input())
    print "Case #{}: {}".format(i+1, int(output))
