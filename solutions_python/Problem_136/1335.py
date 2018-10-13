

def get_line():
    return raw_input().strip()
     
formatFloatList = lambda s: list(map(float,s.split(' ')))

def standard_input():
    count = int(get_line())
    for i in range(count):
        case = formatFloatList(get_line())
        yield (i+1,case)

def calculate_time(C,F,X,n):
    return C*sum(1.0/(2.0 + F*k) for k in range(0,n)) + X/(2.0 + F*n)

def first_min(f):
    xp = f(0)
    x = f(1)
    i = 1
    while x < xp:
        i += 1
        xp = x
        x = f(i)
    return i - 1
           
def handle_case(case):
    C,F,X = case[0], case[1], case[2]
    n = first_min(lambda k: calculate_time(C,F,X,k))
    return "%.7f" % calculate_time(C,F,X,n)
    
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))
        

if __name__ == '__main__':
    main()