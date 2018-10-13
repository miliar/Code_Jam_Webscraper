from math import sqrt, floor, ceil

def reverse(num):  
    rev = 0    
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num /= 10
    
    return rev
         
def is_palindrome(num):
    return num == reverse(num)

def solve(start, end):
    
    sqrt_end = int(floor(sqrt(end)))
    sqrt_start = int(ceil(sqrt(start)))
    
    count = 0
    i = sqrt_start
    while i <= sqrt_end:
        if (is_palindrome(i)) and (is_palindrome(i**2)):
            count += 1
        i+=1
    
    return count

def main(input_path):
    
    with open(input_path) as f:
        cases = int(f.readline())
        
        for i in xrange(cases):
            line = f.readline()
            line_arr = line.split()
            count = solve(int(line_arr[0]), int(line_arr[1]))
            print "Case #%d: %d" % (i + 1, count)
            
if __name__ == "__main__":
    main('input')