cases = int(input())

def istidy(digits):
    istidy = True
    for i in range(1,len(digits)):
        if(digits[i-1] > digits[i]):
            index = i
            istidy = False
            break

    if istidy:
        return -1
    else:
        return index

def allones(digits,index):
    for i in range(len(digits)):
        if(i == index):
            break
        if(digits[i] != 1):
            return False
    
    return True


def transform(digits):

    index = istidy(digits)
    while(index != -1):

        a = digits[index-1]
        b = digits[index]

        if(a == 1 and b == 0 and allones(digits,index-1)):
            digits.pop(0)
            for i in range(len(digits)):
                digits[i] = 9
            # print(digits)
            return


        if(a == 1):
            #if first digit
            if(index-1 == 0):
                for i in range(index,len(digits)):
                    digits[i] = 9
                digits.pop(index-1)
            else:
                for i in range(index,len(digits)):
                    digits[i] = 9
                digits.pop(index-1)
        else:
            digits[index-1] -= 1
            for i in range(index,len(digits)):
                digits[i] = 9
        
        index = istidy(digits)

    # print(digits)


for c in range(cases):
    count = int(input())
    strdigits = list(str(count))
    digits = [ int(i) for i in strdigits ]

    # if(len(digits) == 1):
    #     print(digits[0])

    transform(digits)
    
    # a = digits[index-1]
    # b = digits[index]
    # if(a == 1):
    string = ""
    for a in digits:
        string += str(a)

    print("Case #{}: {}".format(c+1,string))