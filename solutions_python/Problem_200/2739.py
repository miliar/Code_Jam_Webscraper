# Tidy Numbers
# first line of input is the number of test cases
# for number N, find the last tidy number.

file = open("/mnt/c/Users/Samantha Chhoeu/Desktop/2017_Code_Jam/QualificationRound/input.txt")

t = 0 # number of test cases
i = 0 # test number


def decrement(num):
    last_digit = int(str(num)[-1])
    # inefficient decrement number by the last digit + 1
    num = num-last_digit-1
    # decrement current digit by 1

    return num


def check_tidy(num):
    prev = 0
    integer = ""
    for d in str(num):
        if d.isdigit():
            if int(d)<prev:
                return 0
            else:
                prev = int(d)
        else:
            continue
    return 1



def find_tidy(num):
    #print num
    if check_tidy(num) == 1:
        number = ""
        for char in str(num):
            if char.isdigit():
                number+=char
        print "Case #"+str(i)+":",number
    else:
        not_tidy = 0
        prev = 0
        current = ""
        for d in str(num):
            if not_tidy == 0:
                if int(d)<prev:
                    calc = prev-1
                    #print num,calc
                    current+=str(0)
                    not_tidy = 1
                else:
                    current+=str(d)
                    prev = int(d)

            else:
                current+=str(0)
        current = int(current)
        #print current
        new = decrement(current)
        find_tidy(new)




for line in file:
    if t == 0:
        t = line
    else:
        number = int(line)
        find_tidy(number)

    i+=1
