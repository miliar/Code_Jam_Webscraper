#python prac.py < input.txt > output.txt
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

def numToStr(num):
    return list(map(float,str(num)))

if __name__ == "__main__":
    numberOfCases = int(input())  # read a line with a single integer
  
    for i in range(1, numberOfCases + 1):
        actualNumber = input()
        j = 0
        while(j<actualNumber):
            actual = actualNumber - j
            j = j + 1
            actualString = numToStr(actual)
            charAnterior = 0          
            tidy = True
            for char in actualString:
                ichar = int(char)
                if(ichar < charAnterior):
                    tidy = False;
                charAnterior = ichar
            if (tidy == True):
                j += actualNumber
                break
        print("Case #{}: {} ".format(i, actual))
