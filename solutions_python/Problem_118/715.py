import re, numpy, itertools
from math import sqrt

def check_palindrome(number):
    x = str(int(number))
    if len(x) == 1:
        return True
    half_digits = -((-1*len(x))/2) 
    left = x[:half_digits]
    right = x[half_digits:]
    rev_left = left[::-1][-len(right):]
    return (rev_left == right)
    
def palindromes_generator_digits(digits):
    half_digits = -((-1*digits)/2)    
    start_a = int('1'+'0'*(half_digits-1))
    end_a = int('9'*(half_digits))
    if (digits%2) == 0:  #number of digits: even
        for a in range(start_a,end_a+1):
            yield int(str(a) + str(a)[::-1])
    else:   #number of digits: odd
        for a in range(start_a,end_a+1):
            yield int(str(a) + str(a)[-2::-1])
            
def palindromes_generator(digits_min,digits_max):
    generators = [palindromes_generator_digits(digits) for digits in range(digits_min,digits_max+1)]
    return itertools.chain(*generators)

def num_fair_square(int_min,int_max):
    palindromes = [] #0
    digits_min, digits_max = len(str(int(sqrt(int_min)))), len(str(int(sqrt(int_max))))    
    palindromes = list(palindromes_generator(digits_min,digits_max))
    #Final check
    fair_square = [x*x for x in palindromes]
    #print len(fair_square),
    fair_square = filter(lambda x:(x>=int_min)and(x<=int_max), fair_square)
    #print len(fair_square),
    fair_square = filter(check_palindrome, fair_square)
    #palindromes = [math.sqrt(x) for x in fair_square]
    #if len(fair_square):
        #print len(fair_square), fair_square[:min(len(fair_square),7)]
    return len(fair_square) #palindromes

class Case(object):
    def __init__(self, file_iter=None):
        if not file_iter:
            raise ValueError
        found_numbers = None
        while not found_numbers or len(found_numbers) != 2:
            found_numbers = re.findall(r"\d+",file_iter.next())
        self.int_min, self.int_max = map(int, found_numbers)
        self.check_result()        
    def check_result(self):
        self.result = num_fair_square(self.int_min,self.int_max)
                      
#Reading the input file
with open("C-large-1.in", 'r') as file_obj:
    file_iter = iter(file_obj.readline,'')  #filedata = file.read()
    lawns = []
    try:
        while True:        
            found_number = re.search(r"\d+",file_iter.next())
            if found_number:
                N_cases = int(found_number.group(0))
                cases = [Case(file_iter) for i in range(N_cases)]                
                break
    except (StopIteration, ValueError):
        print len(cases)
        pass

#Writing the output file
output = '\n'.join(['Case #{0}: {1}'.format(n+1,case.result) for n,case in enumerate(cases)])
with open("fair-and-square.out", 'w') as file_obj:
    file_obj.write(output)
