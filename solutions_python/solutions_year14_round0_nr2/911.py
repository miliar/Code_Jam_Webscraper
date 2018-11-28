import sys

def solve(C, F, X):
    possibilities = []    
    cookies = 0.0
    curr_rate = 2.0
    time = 0.0
    last = None
    while True:
        val = (X-cookies)/curr_rate + time
        cookies = 0
        time += C/curr_rate
        curr_rate += F
        if last is None or val < last:
            last = val
        else:
            break
    return last

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        C, F, X = map(float, sys.stdin.readline().split(' '))
        answer = solve(C, F, X)
        print 'Case #{}: {}'.format(i+1, answer)

if __name__ == '__main__':
    main()

