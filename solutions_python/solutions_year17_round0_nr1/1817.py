'''
Google Code Jam 2017 Qualification Round
Problem A. Oversized Pancake Flipper
Solution by Liu Yue <euyuil@gmail.com>
Created at 2017-04-08T19:45:00+0800
'''

def calc(state, length):
    '''
    Calculate one case.
    '''
    arr = list()
    for char in state:
        if char == '+':
            arr.append(True)
        elif char == '-':
            arr.append(False)
        else:
            raise ValueError('The state contains invalid character %s' % char)
    # Special case for length == 0
    if length == 0:
        if all(arr):
            return '0'
        else:
            return 'IMPOSSIBLE'
    # Usual cases
    step_cnt = 0
    end = len(arr) - length
    for i in range(0, end + 1):
        if not arr[i]:
            step_cnt = step_cnt + 1
            for j in range(i, i + length):
                arr[j] = not arr[j]
    if all(arr[-length :]):
        return str(step_cnt)
    return 'IMPOSSIBLE'

def main():
    '''
    The main method for the program.
    '''
    with open('A-large.in') as fin, open('A-large.out', 'w') as fout:
        fin.readline()
        curr = 1
        for line in fin:
            parts = line.split(' ')
            res = calc(parts[0], int(parts[1]))
            fout.write('Case #%d: %s\n' % (curr, res))
            curr = curr + 1

if __name__ == '__main__':
    main()
