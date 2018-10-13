if __name__ == '__main__':
    
    test_cases = int(input())
    for case_no in range(1, test_cases + 1):

        d, n = map(int, input().split(' '))
        k = []
        s = []

        for i in range(n):
            inp = input().split(' ')
            k.append(int(inp[0]))
            s.append(int(inp[1]))

        max_time = -1

        for i in range(n):
            dist = d - k[i]
            time = dist / s[i]
            max_time = max(max_time, time)

        max_speed = d / max_time

        print('Case #%d: %.6f' % (case_no, max_speed))
        
