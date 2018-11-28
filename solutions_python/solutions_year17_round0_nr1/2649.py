def pancakes(s, k):
    s = list(s)
    count = 0

    for i in range(len(s) - k + 1):
        if s[i] == '-':
            count += 1
            for j in range(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'


    if ''.join(s) == '+' * len(s):
        return count

    return 'IMPOSSIBLE'

def main():
    for _ in range(int(input())):
        s, k = input().split()
        print('Case #%d: ' % (_ + 1), end='')
        print(pancakes(s, int(k)))

if __name__ == '__main__':
    main()
