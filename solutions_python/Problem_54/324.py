INPUT = {
    'data': ('int', 'linearray')
}

TEST = ('''\
5
3 26000000 11000000 6000000
3 1 10 11
2 800000000000000000001 900000000000000000001
5 26 11 6 26 11
2 9 12
''','''\
Case #1: 4000000
Case #2: 0
Case #3: 99999999999999999999
Case #4: 4
Case #5: 0
''')

OUTPUT = "%s"

def gcd(a,b):
    while b: a, b = b, a%b
    return a

def main(data):
    nums, num = data[0], data[1:]
    
    # find differences
    diffs = []
    for i in xrange(nums-1):
        diffs.append(abs(num[i] - num[i+1]))
        
    # fold diffs with gcd
    factor = diffs[0]
    for i in xrange(1,nums-1):
        factor = gcd(factor, diffs[i])
        if factor == 1:
            # great party starts now!
            return 0
    return (factor - (num[0] % factor)) % factor