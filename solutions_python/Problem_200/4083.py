#!/usr/bin/env python

def findTidy(N):
    if N // 10 == 0:
        return N

    number = 0
    power = 0
    countRepeated = 0

    while(N // 10 > 0):
        if N % 10 < (N // 10) % 10:
            number = number + (9 * (10 ** power))
            for i in range(power-1, -1, -1):
                number = number + ((9-(number%10**(i+1))) * (10 ** i))
            N = N - 10
        else:
            number = number + ((N % 10) * (10 ** power))
        
        power = power + 1
        N = N // 10
    
    number = number + (N * (10 ** power))

    return number

def main():  
    T = int(input())

    for i in range(0,T):
        N = int(input())

        lastTidy = findTidy(N)
        
        print("Case #" + str(i+1) + ": " + str(lastTidy))

if __name__ == "__main__":
    main()
