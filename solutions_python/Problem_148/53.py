
def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    T = int(get_line())
    for i in range(T):
        lst = formatIntegerList(get_line())
        N, X = lst[0], lst[1]
        files = formatIntegerList(get_line())
        yield (i+1,(N,X,files))
        
def handle_case(case):
    N,X,files = case
    files.sort()
    result = N
    i,j = 0,N-1
    while i < j:
        if files[i] + files[j] <= X:
            result -= 1
            i += 1
            j -= 1
        else:
            j -= 1
    return str(result)
    
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    