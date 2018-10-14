import sys


def is_tidy(number):
    last = 0
    for digit in str(number):
        if int(digit) < last:
            return  False
        last = int(digit)
    return True


def check_number(number):
    while(not is_tidy(number)):
        last = 0
        t = ""
        add = False
        for n in str(number):
            if last == 0:
                last = int(n)
                continue
            if not add and int(n) < last:
                t += n
                add = True
            elif add:
                t += n
            last = int(n)
        t = int(t)
        t += 1
        number -= t
    return number

counter = 0
test_cases = 0
for line in sys.stdin:
    if counter == 0:
        counter += 1
        test_cases = int(line)
        continue
    print "Case #" + str(counter) + ": " + str(check_number(int(line)))
    if test_cases == counter:
        break
    counter += 1
