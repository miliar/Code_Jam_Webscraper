import math as math

def palin(number):
    return str(number) == (str(number)[::-1])

def perf_square(number):
    a = number & 0xF
    if a > 9:
        return False
    if a != 2 and a != 3 and a != 5 and a != 6 and a != 7 and a != 8:
        r = int(math.floor(math.sqrt(number)+0.5))
        return r*r == number
    return False


if __name__ == "__main__":

    numberOfTests = (int)(input())

    
    for number in range(numberOfTests):
        ranges = [int(a) for a in input().split(' ')]
        
        count = 0
        for x in range(ranges[0],ranges[1]+1):
            if palin(x) and perf_square(x) and palin(int(math.sqrt(x))):
                count += 1
                #print(x)
        print('Case #'+str(number+1)+': '+str(count))
        
    