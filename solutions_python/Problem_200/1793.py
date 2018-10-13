input_file = open('/Users/eunice.lin/Downloads/B-large.in', 'r')

num_cases = input_file.readline()

def has_smaller(number, start):
    print 'number = ', number
    for i in range(start, len(number)-1):
        print 'start = ', start
        print 'i = ', i
        if number[i] > number[i+1]:
            print 'found greater num at index ', i
            return i
    return -1

def decrement_by_one(number, index):
    print 'decre position x = ', index
    if number[index] == '0' or number[index] == 0:
        number[index] = 9
        decrement_by_one(number, index-1)
    else:
       number[index] = int(number[index]) -1
    print ' new number = ', number

def is_tidy(number):
    number = list(number)
    for i in range(len(number)-1):
        print 'i = ', i
        if int(number[i]) > int(number[i+1]):
            print 'not tidy ', number[i] , '> ' , number[i+1]
            return False
    print 'is tidy'
    return True

i = 1
tidy_num = 0
result = ''
for number in input_file:
    n = 0
    print "~~~~~~~~~~~~~~~"
    number = list(number)
    del number[-1]
    print 'start number = ', number
    number = [int(d) for d in number]
    while not is_tidy(number):
        for x in range(len(number)):
            print "****current digit = ", number[x]
            index = has_smaller(number, x)
            print 'passing in index = ', index
            if index >= 0:
                print 'number = ', number
                decrement_by_one(number, index)
                for y in range(index+1, len(number)):
                    print 'set pos y = ', y, ' to 9'
                    number[y] = '9'
                break
        print "end of loop number = ", number
    number = "".join(str(d) for d in number)
    number = str(int(number))
    result += "Case #{}: {}\n".format(i, number)
    i += 1

output_small = open('./result-largeB.txt', 'w+')
output_small.write(result)


