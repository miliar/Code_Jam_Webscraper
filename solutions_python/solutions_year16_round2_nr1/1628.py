DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def is_digit(str_digit, str_input):
        
        if len(str_digit) == 0:
            return True, str_input
    
        if str_digit[0] in str_input:
            new_input = str_input.replace(str_digit[0], "", 1)
            return is_digit(str_digit[1:],new_input)
        else:
            return False, ""

def find(str_input, number):
    
    if not str_input.isalpha():
        return number
    
    for i in range(0, len(DIGITS)):
        check, new_input = is_digit(DIGITS[i], str_input)
       
        if check:
            result = find(new_input, number + str(i))
            if result != None:
                return result
    
    return None
               

def solve(str_input):    
    str_input = str_input.replace('\n', '')
    return find(str_input, "")

# Read file
with open('input.txt') as f:
    content = f.readlines()

f_output = open("output.txt", "wb")
for i in range(1, int(content[0]) +1):
    f_output.write("Case #" + str(i) + ": " +solve(content[i]) + "\r\n");
f_output.close()