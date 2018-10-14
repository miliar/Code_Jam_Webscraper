#B prob
import math

def Dance():
    test_cases = int(raw_input())
    for test in range(test_cases):
        input = raw_input().split()
        N, S, P = int(input[0]),  int(input[1]),  int(input[2])
        scores = map(int, input[3:])
        cnt = 0
        scores.sort()
        for score in reversed(scores):
            if score >= (3 * P - 2):
                cnt += 1
            elif score >= math.fabs((3 * P - 4)) and S > 0:
                cnt += 1
                S -= 1
            else:
                break
        
        print 'Case #%d:'%(test+1), cnt
        

if __name__ == '__main__':
    Dance()
