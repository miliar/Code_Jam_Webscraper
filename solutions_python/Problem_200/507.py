def main():
    t = int(input().strip())
    for case in range(1, t + 1):
        n = int(input().strip())
        last = list(map(int, str(n)))
        while not istidy(last):
            fixfirstprob(last)
        s = ''.join(map(str, last))
        s = s.lstrip('0')
        print('Case #{}: {}'.format(case, s))

def istidy(num):
    return all(num[i] <= num[i+1] for i in range(len(num) - 1))

def fixfirstprob(num):
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            num[i] -= 1
            for j in range(i + 1, len(num)):
                num[j] = 9
    return

if __name__ == '__main__':
    main()
    
