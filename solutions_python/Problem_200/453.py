def rec_attempt(num, digit):

    if(digit < len(num)-2):
        if(num[digit+1] < num[digit+2]):
           return True
        if(num[digit+1] > num[digit+2]):
           return False
        return rec_attempt(num, digit+1)
    return True


t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):

    power_game = False
    num = raw_input()
    out = ''
    for digit in range(len(num)):
        if(power_game):
            out += '9'
            continue
        if(digit != len(num)-1):
            if(int(num[digit]) < int(num[digit+1])):
                out += num[digit]
            elif(int(num[digit]) == int(num[digit+1])):
                if(rec_attempt(num, digit)):
                    out += num[digit]
                else:
                    temp = str(int(num[digit])-1)
                    power_game = True
                    if(temp == '0' and out == ''):
                        continue
                    out += temp
            else:
                temp = str(int(num[digit])-1)
                power_game = True
                if(temp == '0' and out == ''):
                    continue
                out += temp
        else:
            out += num[digit]

    print "Case #{}: {}".format(i, out)
