input = open("B-small-attempt0.in" , 'r')
output = open("ouput.txt" , 'w')

testCases = int(input.readline().replace('\n' , ''))

def tidyCheck (rat):
    string = str(rat)
    for _ in range(len(string)-1):
        if string[_] > string[_+1]:
            return False

    return True

def outputWrite ( num , rat):
    out = "Case #" + str(num) + ": " + str(rat) +"\n"
    output.write(out)



for _ in range(testCases):
    x = int(input.readline().replace("\n" , ""))
    while True:
        if len(str(x)) == 1:
            outputWrite(_+1 , x)
            break
        if tidyCheck(x):
            outputWrite(_ +1, x)
            break
        else:
            x = x-1
            #TODO  needs some other algorithm to decrement the number



input.close()
output.close()