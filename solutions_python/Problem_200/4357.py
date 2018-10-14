times = input()

def isTidy(number):
    tidy = [int(i) for i in list(str(number))]
    number_str = ''.join(str(i) for i in tidy)
    tidy.sort()
    tidy_str = ''.join(str(j) for j in tidy)
    if  number_str == tidy_str: 
        return 0
    else:
        return 1

for i in range(1,times+1):
    number = input()
    while isTidy(number):
        number -= 1
        if(number < 10):
            break

    print "Case #{0}: {1}".format(i, number)
