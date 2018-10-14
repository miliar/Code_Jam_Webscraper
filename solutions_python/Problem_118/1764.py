import sys, math

#Yes, the number is backwards. No, I don't need to correct this.
def getDigitArray(number):
    result = []
    while number != 0:
        result.append(number%10)
        number = math.floor(number/10)
    return result
    
def getNumberOfGood(start, end):
    start_root = math.floor(math.sqrt(start))
    end_root = math.floor(math.sqrt(end))
    count = 0
    for n in range(len(str(start_root)), len(str(end_root))+1):
        number = [0]*math.ceil(n/2)
        number[0] = 1
        
        while number[-1] < 10:
            root = 0
            for x in range(len(number)):
                if x == (len(number) - 1) and n%2 == 1:
                    root += number[x]*pow(10, x)
                else:
                    root += number[x]*pow(10, x) + number[x]*pow(10, n-x-1)
            square = root*root
            if start <= square <= end:
                square = getDigitArray(square)
                square_len = len(square)
                valid = True
                for x in range(math.floor(square_len/2)):
                    if square[x] != square[square_len-x-1]:
                        valid = False
                        break
                if valid:
                    count += 1
            #    print(repr(number) + "  --  " + repr(root) + " -- " + repr(root*root)+":"+repr(valid))
            #else:
            #    print(repr(number) + "  --  " + repr(root) + " -- " + repr(root*root)+":False")
            
            i = 0
            number[i] += 1
            while number[i] >= 10 and i < len(number)-1:
                number[i] = 0
                i += 1
                if i >= len(number):
                    break
                number[i] += 1
            if number[0] == 0:
                number[0] = 1
    return count

def main():
    #print( getNumberOfGood(0, math.pow(10,24)) )
    #return
    #f = open("test", "r")
    f = sys.stdin
    
    num = int(f.readline())
    for i in range(num):
        line = f.readline().split(" ")
        print("Case #"+str(i+1)+": ", end='')
        print( getNumberOfGood( int(line[0]), int(line[1]) ) )

    #f.close()

if __name__ == '__main__':
    main()
