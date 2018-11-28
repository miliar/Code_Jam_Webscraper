INPUT = {
    'total': ('int', 'constant'),
    'candies': ('int', 'linearray')
}

INPUT_ORDER = ['total', 'candies']

TEST = ('''\
2
5
1 2 3 4 5
3
3 5 6
''','''\
Case #1: NO
Case #2: 11
''')

def xor(a,b):
    return a^b

def main(total, candies):
    if reduce(xor, candies) != 0:
        return "NO"
    else:
        candies.sort()
        candies.reverse()
        candies.pop()
        return sum(candies)