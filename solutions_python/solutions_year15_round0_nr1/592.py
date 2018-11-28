def do():
    times = input()
    for i in xrange(times):
        print 'Case #%d:'%(i+1),
        calculate()

def calculate():
    n,man = raw_input().split()
    
    many = 0
    stand = 0
    
    for i,digit in enumerate(man):
        digit = int(digit)
        if digit == 0:
            continue

        if i > stand:
            many += i-stand
            stand = i
        stand += digit
    
    print many



if __name__ == '__main__':
    do()

