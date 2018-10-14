def answer(s):
    if len(s) == 1:
        return s.pop()
    elif len(s) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'
    

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        first = int(input())-1
        A = set()
        for line in range(4):
            for x in input().split():
                if line == first:
                    A.add(int(x))
                    
        second = int(input())-1
        B = set()
        for line in range(4):
            for x in input().split():
                if line == second:
                    B.add(int(x))
        A &= B
        print('Case #{}: {}'.format(case+1, answer(A)))
