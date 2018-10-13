import math

def is_palindrome(x):
    x = str(x)
    if(x == x[::-1]):
        return True
    else:
        return False

    
def is_int(x):
   x = str(x)
   x = x.split('.')
   if(x[1] == '0'):
       return True
   return False

def quest():
    output = 0
    inpt = raw_input()
    inpt = inpt.split(" ")
    begin = int(inpt[0])
    end = int(inpt[1])
    
    for i in range(begin,end+1):
        sqrt = math.sqrt(i)
        if(is_palindrome(i) and is_int(sqrt)and is_palindrome(int(sqrt))):
            output +=1
    
    return str(output)

def print_output(i, output):
    print 'Case #' + str(i+1) + ': ' + output
    
##############################################
n_cases = input()

for i in range(n_cases):
    output = quest()
    print_output(i, output)
