def nextDigit(predigit, remainder, divN):
    if predigit > remainder /divN:
        return -1
    else:
        if divN == 1:
            return 1
        else:
            return nextDigit(remainder / divN ,remainder % divN,divN /10)
T = input()
count = 1
while T > 0:
    l = raw_input()
    int_l = int(l)
    while int_l > 0:
        copy_l = str(int_l)
        length = len(copy_l)
        preDigit = int_l/(10**length)
        boole = nextDigit(preDigit,int_l % (10**length),10**(length-1))

        if boole == 1:
            print "Case #" + str(count) + ": "+ str(int_l)
            count += 1
            break
        else:
            int_l -= 1
    T -= 1