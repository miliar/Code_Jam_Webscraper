from math import pow

def main():
    fin = open("C-small-attempt0.in", "rt")

    count = int(fin.readline())
    output = ""

    for x in range(count):

        lower, upper = fin.readline().strip("\n").split(" ")
        count = fairAndSquare(float(lower), float(upper))
        
        output += str.format("Case #{0}: {1}\n", x+1, count)


    fin.close()

    fout = open("C-small.out", "wt")
    fout.write(output)
    fout.close()

def checkPalindrome(value):

    value = str(value)
    reverse = ""
    stack = []
    
    for char in value:
        stack.append(char)

    for x in range(len(value)):
        reverse += stack.pop()

    return value == reverse

def fairAndSquare(lower, upper):

    count = 0

    theoUpper = int(pow(upper, 0.5))
    theoLower = int(pow(lower, 0.5))
    
    for i in range(theoLower, theoUpper+1):
        
        if checkPalindrome(i):
            power = int(pow(i,2))
            
            if power >= lower and power <= upper and checkPalindrome(power):
                count += 1

    return count

main()
