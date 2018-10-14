def rdline():
    return map(int,raw_input().split())

def get_ans():
    row = int(raw_input())
    rows = [rdline() for x in range(4)]
    return set(rows[row-1])
    
def solve_one():
    s1 = get_ans()
    s2 = get_ans()
    s = s1.intersection(s2)
    if len(s) == 0:
        return 'Volunteer cheated!'
    elif len(s) == 1:
        return str(s.pop())
    else:
        return 'Bad magician!'

def main():
    T = int(raw_input())

    for s in range(1,T+1):
        print ('Case #%d: ' % s) + solve_one()


if __name__ == '__main__':
    main()
