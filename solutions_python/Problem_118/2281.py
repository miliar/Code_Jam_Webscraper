import sys
import math

def palindrome(number):
    num_digits = int(math.log10(number))
    for i in range(num_digits/2 + num_digits%2):
        digit1 = (number / 10**(num_digits-i)) % 10
        digit2 = (number / 10**i) % 10
        if digit1 != digit2:
            return False
    return True

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        lines = f.readlines()
    
    num_cases = int(lines[0])
    
    for case in range(num_cases):
        answer = 0
        interval = tuple(int(s) for s in lines[case+1].split())
        start = int(math.ceil(math.sqrt(interval[0])))
        end = int(math.sqrt(interval[1]))
        for number in range(start,end+1):
            if palindrome(number) and palindrome(number**2):
                answer += 1
        print "Case #%s: %s"%(case+1, answer)
    
