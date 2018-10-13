import io
from array import array
import itertools
from itertools import chain

input_stream = io.StringIO('''5
1 4
10 120
100 1000
1 1100000
1 100000000000000
1 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
''')

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def read_endpoints(f):
    return [int(v) for v in f.readline().split()]

def process_endpoints(A, B):
    sqrt_A = isqrt(A)
    sqrt_B = isqrt(B)
    A_ndigits = len(str(sqrt_A))
    B_ndigits = len(str(sqrt_B))
    total = 0
    for ndigits in range(B_ndigits+1, A_ndigits - 1, -1):
        #print('calc for: %d' % ndigits)
        total += calc(ndigits, A, B)
    return total

def calc(ndigits, square_min_value, square_max_value):
    npalindromes = 0
    if ndigits == 1:
        for v_square in [1, 4, 9]:
            if v_square >= square_min_value and v_square <= square_max_value:
                #print('palindrome: %s, min: %s, max: %s' % (v_square, square_min_value, square_max_value))
                npalindromes += 1
        return npalindromes
    
    palindrome = array('B', (0 for i in range(ndigits)))
   
    first_range = range(1, 10)
    ranges_after_first_count = ndigits//2 - 1 if ndigits % 2 == 0 else ndigits//2
    digit_ranges_after_first = [range(10) for i in range(ranges_after_first_count)]
    foundvalues = set()
    for lst in itertools.product(*chain([first_range], digit_ranges_after_first)):
        for i, d in enumerate(lst):
            palindrome[i] = d
            palindrome[ndigits - i - 1] = d
            value = array_to_int(palindrome)
            if value not in foundvalues:
                foundvalues.add(value)
                #print ('considered value: %s' % (value))
                value_square = value**2
                if value_square >= square_min_value and  value_square <= square_max_value and is_palindrome(value_square):
                    #print (value)
                    npalindromes += 1
    return npalindromes

def is_palindrome(n):
    nstr = str(n)
    return nstr == ''.join(reversed(nstr))

def array_to_int(arr):
    #return int(''.join(str(i) for i in arr))
    size = len(arr)
    v = 0
    m = 1
    for i in range(size):
        v += m * arr[-i - 1]
        m *= 10
    #print (arr, v)
    return v


def main(input_stream):
    for i in range(int(input_stream.readline())):
        A, B = read_endpoints(input_stream)
        result = process_endpoints(A, B)
        print('Case #%d: %d' %(i+1, result))
    
    

if __name__ == '__main__':
    #main(input_stream)
    import sys
    main(open(sys.argv[1]))