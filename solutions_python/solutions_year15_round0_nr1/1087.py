def f(data):    
    s = data[0]
    for i in range(1, len(data)):
        if s < i:
            yield i - s
            s = i 
        s += data[i]
        
def solution(string):
    return sum(f(list(map(int,string))))

def parse(inputfilename):
    it = iter(open(inputfilename))
    N = int(next(it))
    for i in range(N):
        line = next(it)
        print("Case #{}: {}".format(i+1, solution(line.split()[1])))
        
parse("A-large.in")