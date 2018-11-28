# we want numbers that are tidy, that is, are in increasing order
# we start with a number and find the largest number that is tidy that is less than it.
# how will we find this? we start on the right side and start going over until we find a number greater. then we borrow the ten's column and make a nine. keep on going
# 123, 555, 488, 8999, 11299 are all tidy

for T in range(1, int(input())+1):
    # get number
    raw = input()
    number = int(raw)
    digits = [int(x) for x in list(raw)]
    # start at the right and work towards the left
    digits = list(reversed(digits))
    lastdigit = 9
    index = 1
    while index < len(digits):
        #print("index = " + str(index) + " digits are " + str(list(reversed(digits))))
        if digits[index - 1] < digits[index]:
            # we're not tidy
            # pull one from digits[index]
            digits[index] -= 1
            # set all digits from 0 to (index - 1) to 9
            for x in range(0, index):
                digits[x] = 9
            #digits[index-1] = 9 old code that didn't work
            # set index back to 1
            # index = 1 EDIT: not necessary if all prior digits are set to 9
        index += 1
    str_to_print = ""
    for digit in list(reversed(digits)):
        str_to_print += str(digit)
    print("Case #" + str(T) + ": " + str(int(str_to_print)))


