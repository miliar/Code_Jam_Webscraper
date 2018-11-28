"""
Input

Output

4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

"""

def is_tidy(n):
    digits = map(int, list(str(n)))

    for i in xrange(len(digits)-1):
        if (digits[i] > digits[i+1]):
            return False

    return True

def nearest_tidy(n):
    for i in xrange(n):
        x = n-i
        if is_tidy(x):
            return x

def run(input):
    lines = str.split(input, '\n')[1:]
    for i in xrange(len(lines)):
        n = int(lines[i])
        t = nearest_tidy(n)
        print('Case #%d: %d'%(i+1, t))

if __name__ == '__main__':
    with open('B-small-attempt0.in', 'r') as f:
        input = f.read().strip()
        run(input)
