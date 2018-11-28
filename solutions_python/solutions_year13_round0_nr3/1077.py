import gmpy

def isFine(stringInteger):
    """Returns true if integer is 'fine', if integer's digits are a palindrome    
    Arguments:
    - `stringInteger`: Integer's digits
    """
    size = stringInteger.__len__()
    half_size = size / 2;
    
    if size == 1:
        return True;
    
    if (size % 2 == 0):
        last_half = stringInteger[half_size::]
    else:
        last_half = stringInteger[half_size+1::]

    reversed_last_half = last_half[::-1]

    if stringInteger.startswith(reversed_last_half):
        return True
    else:
        return False

f = open('C-small-attempt0.in', 'r')
o = open('output.txt', 'w')

Cases = int(f.readline().strip())

for t in xrange(Cases):
    original_limits = [gmpy.mpz(x) for x in f.readline().split()]
    gmp_limits = [gmpy.mpz(x) for x in original_limits]
    cropped_gmp_limits = [x.root(2) for x in gmp_limits]

    if cropped_gmp_limits[0][1] == 1:
        gmp_range = [gmpy.mpz(x) for x in range(cropped_gmp_limits[0][0], cropped_gmp_limits[1][0]+1)]
    else:
        gmp_range = [gmpy.mpz(x) for x in range(cropped_gmp_limits[0][0] + 1, cropped_gmp_limits[1][0]+1)]
        
    fine_range = [x for x in gmp_range if isFine(x.digits(10)) == True]

    squared_fine_range = [x * x for x in fine_range]

    fine_and_square_list = [x for x in squared_fine_range if isFine(x.digits(10)) == True]
    #print fine_and_square_list
    
    s = "Case #%d: %s\n" % (t+1, len(fine_and_square_list))
    print s
    o.write(s)
