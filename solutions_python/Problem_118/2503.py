import math

DEBUG = False

def check_sqrt(number):
    sqrt = math.sqrt(number)
    return sqrt == math.trunc(sqrt)

def process_data(data, case_number, f_out):
    if DEBUG:
        print 'Case #%s: ' % (case_number + 1)
    else:
        f_out.write('Case #%s: ' % (case_number + 1))
    
    count = 0
    for number in range(data[0], data[1] + 1):
        if str(number) == str(number)[::-1]:
            if check_sqrt(number):
                sqrt = str(int(math.sqrt(number)))
                if sqrt == sqrt[::-1]:
                    count += 1
    
    if DEBUG:
        print count
    else:
        f_out.write('%s\n' % count)
    return
    
loc_in = r'c:\coding\codejam\problemC\data.in'
loc_out = r'c:\coding\codejam\problemC\data.out'
    
with open(loc_in, 'rb') as f_in:
    with open(loc_out, 'wb') as f_out:
        num_of_cases = f_in.next()
        
        for case_number in xrange(int(num_of_cases)):
            try:
                data = [int(x) for x in f_in.next().strip('\n').split(' ')]
                process_data(data, case_number, f_out)
            except StopIteration:
                break