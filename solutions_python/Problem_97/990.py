def all_same_number(test_number):
    test_number = list(str(test_number))
    for test_digit in range(0,len(test_number)-1):
        if test_number[test_digit] != test_number[test_digit+1]:
            return False
    return True

def combinations_for_number(num):
    num = list(str(num))
    combinations = []
    for eachdigit in range(len(num)):
        combinations.append(int("".join(num[eachdigit:] + num[:eachdigit])))
    del combinations[0]
    return combinations

def is_recycled_pair(n,m):
    if m in combinations_for_number(n):
        return True
    else:
        return False

text_file = open("C_input.txt", "r")
input_text = text_file.readlines()
run_amount = int(input_text[0])
for testcase in range(1,run_amount+1):
    #print "Case #" + str(testcase)
    data = input_text[testcase].split()
    low,high = int(data[0]), int(data[1])
    numbers = range(low,high+1)
   #print numbers
    amount = 0
    for number in numbers:
        for eachcombination in combinations_for_number(number):
            if int(eachcombination) >= low and int(eachcombination) <= high:
                if is_recycled_pair(number,eachcombination):
                    if not all_same_number(eachcombination):
                        if not eachcombination <= number:
                            amount += 1
                            #print "DONE!",number,eachcombination
    print "Case #" + str(testcase) + ": " + str(amount)
