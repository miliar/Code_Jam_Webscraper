
def solve(f) :
    first_guess = int(f.readline())
    for i in range(4) :
        row = f.readline().split()
        row = [ int(cell) for cell in row ]
        if i == first_guess - 1 :
            s1 = set(row)
            
    second_guess = int(f.readline())
    for i in range(4) :
        row = f.readline().split()
        row = [ int(cell) for cell in row ]
        if i == second_guess - 1 :
            s2 = set(row)
    s = s1 & s2
    if len(s) == 0 :
        return 'Volunteer cheated!'
    elif len(s) == 1 :
        return str(s.pop())
    else :
        return 'Bad magician!'        

if __name__ == '__main__' :
    with open('A-small-attempt1.in') as f:
        t = int(f.readline())
        for i in range(t) :
            print ('Case #{0}: {1}'.format(i + 1, solve(f)))
