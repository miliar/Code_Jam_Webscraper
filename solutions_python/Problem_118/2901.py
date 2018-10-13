import math
def isPalindrome(x):
    a = str(x)
    if a == '' or len(a) == 1:
        return True
    elif a[0] == a[-1]:
        return isPalindrome(a[1:-1])
    else:
        return False
def is_square(n):
    return math.sqrt(n).is_integer()

def NRsqrt(x):
    '''
    Function approximates the square root of x (float)
    using Newton-Rhapson method such that sqrt(x)**2 - x is within epsilon of 0
    '''
    guess = x/2.0
    epsilon = 0.0001
    while abs(guess*guess - x) >= epsilon:
        guess = guess - ((guess**2 - x)/(2*guess))
    return int(guess)



kupka = open('rizaltyy.txt', 'w')


inFile = open('C-small-attempt2.in', 'r')
lines = inFile.readlines()


cases = lines[0]
pairs = []
for case in range(int(cases)):
    pairs.append(lines[case+1].rsplit(' '))


for case in range(int(cases)):
    fairs = 0
    for number in range(int(pairs[case][0]), int(pairs[case][1])+1):
        if isPalindrome(number) and is_square(number) and isPalindrome(NRsqrt(number)):
            fairs += 1
    wynik = 'Case #' + str((case + 1)) + ': ' + str(fairs)
    kupka.write(wynik+'\n')
    kupka.flush()

kupka.close()
    



    


    

