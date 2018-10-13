OUTPUT_FILENAME = "SampleOuput.txt"
TOPLOW = 10000000

import pickle

def getLow():
    polies = []

    i = 0
    while i < TOPLOW:
        if isPoly(i):
            polies.append(i)
        i += 1
        
    return polies
    
def isPoly(num):
    digits = getDigits(num)
    length = len(digits)
    for i in range(length/2):
        if (digits[i] != digits[length - 1 - i]):
            return False
            
    return True
    
def getDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num / 10
        
    digits.reverse()
    
    return digits
    
def get_all():
    all = []
    polies = getLow()
    for p in polies:
        if isPoly(p * p):
            all.append(p*p)
            
    return all
    
def output_all(all_polies):
    f = open("polies7.p", 'w')
    pickle.dump(all_polies, f)
    f.close()
    
if __name__ == "__main__":
    all = get_all()
    output_all(all)