def is_square(x):
    a = x**0.5
    b = int(a)
    if(b*b == x):
        return True
    else:
        return False
def is_palindrome(a):
    if a<10:
        return True
    else:
        x = a
        x_array = [];
        while(x>=10):
          remainder = x%10
          x_array.append(remainder)
          x = x/10;
        x_array.append(x)
        rev = 0
        place = len(x_array)-1
        for i in x_array:
            rev += i*(10**place)
            place = place - 1
        if rev == a:
            return True
        else:
            return False
def check_is_fair_and_square(x):
    if is_square(x) is False:
        #print "stage a fails"
        return False
    else:
        if is_palindrome(x) is False:
            #print "stage b fails"
            return False           
        else:
            root = int(x**0.5)
            if is_palindrome(root) is True:
                return True
            else:
                #print x
                #print "stage c fails"
                return False
                
        
def game_func(a, b):
    num = 0
    for i in range(a, b+1):
        if check_is_fair_and_square(i) is True:
            num += 1

    return num

input = open('C-small-attempt0.in', 'r')
T = int(input.readline())
for i in range(0, T):
    text = input.readline()
    temp = text.split("\n")[0]
    a = temp.split(" ")[0]
    b = temp.split(" ")[1]
    #print a
    #print b
    result = game_func(int(a), int(b))
    #print result
    print "Case #" + str(i+1) + ": " + str(result) 


