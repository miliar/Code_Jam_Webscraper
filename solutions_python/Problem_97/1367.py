map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q'}

def rotate(s, amount):
    return s[-amount:] + s[:-amount]

def count_numbers(a, b):
    count = 0
    for i in range(a, b + 1):
        table = set()
        s = str(i)
        for amount in range(1, len(str(i))):
            s = rotate(str(i), amount)
            if s not in table and int(s) <= b and len(s) == len(str(i)) and i < int(s):
            #    print '(' + str(i) + ', ' + s + ')'
                table.add(s)
                count += 1
            #else:
            #   print 'bad: (' + str(i) + ', ' + s + ') - ', s not in table, int(s) <= b , len(s) == len(str(i)),  i < int(s)

    return count

with open('in.txt') as f:
    f.readline()
    lines = f.readlines()
    for line, i in zip(lines, range(len(lines))):
        a, b = [int(x) for x in line.split()]
        print "Case #" + str(i + 1) + ': ' + str(count_numbers(a, b))