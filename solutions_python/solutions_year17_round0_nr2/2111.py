def tidy(number):
    l = len(number)
    for i in range(0,l-1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True


def decrease(number, i):
    target = int(number[i])
    l = len(number)*(-1)

    head = ""
    previous = ""
    tail = ""

    # do parsing
    if i -1 < l:
        head = ''
    else:
        head = number[:i-1]
    previous = number[i-1]
    tail = number[i:]

    # Do decrease
    if previous == '1' and head == '' :
        previous = ''
    else:
        previous  = str(int(previous )-1)

    nnines = len(tail)
    tail = "" + nnines*'9'

    return head + previous + tail

def lasttidy(number):
    l = len(number)
    if tidy(number):
        return number

    for i in range(1,l):
        ii = i*(-1)
        if number[ii] < number[ii-1]:
            number = decrease(number, ii)
    return number

def main():
    # read number of tests
    ntests = int(input())

    for t in range(0, ntests):
        # read last number counted
        number = input()

        print("Case #{}: {}".format(t+1, lasttidy(number)))

if __name__ == '__main__':
    main()
