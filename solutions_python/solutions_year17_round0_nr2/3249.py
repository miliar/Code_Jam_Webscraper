"""CodeJam 2017"""

def read(file_name):
    with open(file_name, 'r') as ifile:
        return ifile.readlines()
    
def solver(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num /= 10
    new_digits = make_tidy(digits)
    r = 0
    for d in reversed(new_digits):
        r = r*10 + d
    return r

def make_tidy(digits):
    for i, d in enumerate(digits):
        if i+1 >= len(digits):
            continue
        if d < digits[i+1]:
            j = 0
            while j <= i:
                digits[j] = 9
                j += 1
            digits[i+1] -= 1
    return digits

def main():
    file_name = 'B-large.in'
    lines = read(file_name)
    tests = lines[1:]
    for i, test in enumerate(tests):
        r = solver(long(test))
        print 'Case #{}: {}'.format(i+1, r)

if __name__=='__main__':
    main()