# Problem A - Counting sheep
def openfile(filename, separator = False):
    # Open the .in file specified by filename as a string 
    # Split it into a list (using the separator if specified)
    # Return that list    
    string = open(filename).read()
    if separator == False: return string.split()
    return string.split(separator)

input_filename = 'B-large.in'
output_filename = 'B-large-output.in'

def main(input_filename, output_filename):
    
    lis = openfile(input_filename)
    output_file = open(output_filename,'w')
    
    for i in range(1,int(lis[0])+1):
        text = 'Case #{}: {}\n'.format(i, elegant(lis[i]))
        output_file.write(str(text))

# MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

def istidy(n):
    # int n
    # Input must be free of leading 0s
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]): return False
    return True

def brute(n):
    # int n
    while not istidy(n):
        n -= 1
    return n

def elegant(n):
    # int n
    n = int(n)
    
    if istidy(n): return n    
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            res = s[:i] # up to but not including i
            res += str(int(s[i])-1)
            res += '9'*100
            res = res[:len(s)]
            break
    return elegant(int(res))

'''nput 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999'''