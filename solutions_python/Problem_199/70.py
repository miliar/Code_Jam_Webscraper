
def pank(d):
    if d == '-':
        return 1
    elif d == '+':
        return 0
    else:
        raise Exception('I know Python!')
        
def solve(case):
    pan,num = input().split()
    pan = [c == '-' for c in pan]
    num = int(num)

    hits = 0

    for i in range(len(pan)-num+1):
        if pan[i] == 1:
            hits += 1
            for j in range(num):
                pan[i+j] = 1 - pan[i+j]

    for i in range(len(pan)):
        if pan[i] == 1:
            print('Case #%d: IMPOSSIBLE' % (case+1))
            return
    print('Case #%d: %d' % (case+1,hits))
    return

q = int(input())
for case in range(q):
    solve(case)
            


