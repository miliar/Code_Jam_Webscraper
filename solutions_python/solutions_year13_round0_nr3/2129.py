def open_file (filename='input.txt'):
    fin = open(filename, 'r')
    lines = fin.read().split('\n')
    if lines[-1] == '':
        lines = lines[:-1]
    fin.close()

    return lines

def parse_file(lines):
    interval_count = int(lines[0])
    intervals = [[int(x),int(y)] for x,y in [line.split(' ') for line in lines[1:]]]

    return intervals

def is_palindrome (num):
    num_rev = list(str(num))
    num_rev.reverse()
    
    return list(str(num)) == num_rev

def check_interval (interval):
    x, y = interval
    fairsquares = [1,4,9,121,484]
    result = 0
    for  num in fairsquares:
        if num >= x and num <= y:
            result += 1
            
    return str(result)

if __name__ == "__main__":
    fout = open('output.txt', 'w')
    intervals = parse_file(open_file())

    for i,interval in enumerate(intervals):
        fout.write('Case #' + str(i+1) + ": " + check_interval(interval) + '\n')

    fout.close()
    print 'Done'

##    for i in xrange(1,1000):
##        if is_palindrome(i):
##            if is_palindrome(i**2):
##                print i**2
