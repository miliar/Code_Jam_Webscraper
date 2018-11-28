
def exists_in(item,array):
    try:
        if array.index(item) >= 0:
            return True
    except ValueError:
        return False

def do_case(exists,create):
    answer = 0
    cache = exists
    for case in create:
        while not exists_in(case,cache) and case:
            idx = case.rfind('/')
            ncase = case[:idx]
            cache.append(case)
            answer +=1
            case = ncase
    return answer

def do(inp):
        lines = inp.split('\n')
        T = int(lines[0])
        cases = lines[1:]
        result = ""
        for t in range(T):
                n,m = map(int,cases.pop(0).split(' '))
                exists,create,cases  = cases[:n],cases[n:n+m],cases[n+m:]
                answer = do_case(exists,create)
                result += "Case #%s: %s\n" % (str(t+1),answer)
        return result
        
if __name__ == '__main__':
    filename = 'A-large'
    #filename = 'mini'
    inp = open('%s.in' % filename).read()
    r = do(inp)
    open('%s.out' % filename,'w').write(r)

