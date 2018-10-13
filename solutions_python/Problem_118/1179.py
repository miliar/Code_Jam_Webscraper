import re
import math


def next_palindrome(num):
    if not is_palindrome(num):
        return create_palindrome(num)
    return palindrome_rec(list(str(num)))

def create_palindrome(number):
    string = list(str(number))
    for i in range(len(string) / 2):
        string[len(string) - i - 1] = string[i]
    return int("".join(string))

#Mehtod to check if a number is palindrome or not?
def is_palindrome(num):
    string = str(num)
    for i in range(len(string) / 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def palindrome_rec(digit_list,offset=0):   
    length = len(digit_list)
    upper = length / 2 + offset
    lower = length / 2 - offset
    if length % 2 == 0:
        lower -= 1
    if lower < 0:
        new_list = ["0" for i in range(length-1)]
        new_list.insert(0,"1")
        new_list.append("1")
        return int("".join(new_list))
    new_digit = (int(digit_list[upper]) + 1) % 10
    digit_list[upper] = str(new_digit)
    digit_list[lower] = str(new_digit)
    if new_digit == 0:
        return palindrome_rec(digit_list,offset+1)
    return int("".join(digit_list))


#Mehtod to count no. of Palindrome
def count_palindromes(lower,upper):
    count = 0
    cur = next_palindrome(lower) if not is_palindrome(lower) else lower
    
    while cur <= upper:
        num = math.sqrt(cur)
        sqint = int(num)
        if cur >= lower and is_palindrome(sqint) and sqint == num:
            
            count += 1
        else:
            pass
            
        cur = next_palindrome(cur)
        
    return count


def fairbound(f):
    bounds = re.split(" ",f.readline())
    return count_palindromes(long(bounds[0]),long(bounds[1]))


def fairsquare():
    output = []
    with open("C-small-attempt0.in","r") as f:
        trials = f.readline()
        for i in range(int(trials.strip())):
            outline = "Case #%d: %s" % (i+1, fairbound(f))
            print outline
            output.append(outline)
    with open("fairsquare_small.out","w") as f:
        f.write("\n".join(output))



if __name__ == "__main__":
    fairsquare()