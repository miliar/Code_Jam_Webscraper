def main():
    inputfile = open("C-large.in", 'r')
    outputfile = open("output", 'w')
    currentcase = 1
    totalcase = int(inputfile.readline().strip())
    while currentcase <= totalcase:
        totalcandy = int(inputfile.readline().strip())
        candybag = inputfile.readline().strip().split()
        candybag = [int(i) for i in candybag]
        candybag.sort()
        candybag2 = [binary(i) for i in candybag]
        index = 1
        length = len(candybag2)
        total = candybag2[0]
        while index < length:
            total = binaryplus(total, candybag2[index])
            index += 1
        length = len(total)
        index = 0
        equal0 = True;
        while index < length and equal0:
            if total[index] != '0':
                equal0 = False
            index += 1
        output = ''
        if not equal0:
            output = 'NO'
        else:
            output = str(sum(candybag) - candybag[0])
        output = "Case #%d: %s\n" %(currentcase, output)
        outputfile.write(output)
        currentcase += 1
    outputfile.close()
    inputfile.close()
    
def binary(number):
    s = number%2
    shang = (number - s)/2
    if shang:
        return binary(shang) + str(s)
    else:
        return str(s) 

def binaryplus(number1, number2):
    len1 = len(number1)
    len2 = len(number2)
    minlen = min(len1, len2)
    difference = abs(len1 - len2)
    index = 1
    s = ''
    while index <= minlen:
        if (number1[-index] == '0' and number2[-index] == '1') or (number1[-index] == '1' and number2[-index] == '0'):
            s = '1' + s
        else:
            s = '0' + s
        index += 1
    if minlen == len1:
        s = number2[0: difference] + s
    else:
        s = number1[0: difference] + s
    return s   
    
if __name__ == "__main__":
    main()
    
