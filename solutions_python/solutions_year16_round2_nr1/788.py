from collections import defaultdict

def solve(S):
    d = defaultdict(int)
    for c in S:
        d[c] += 1
    nums = []
    nums.extend(d['Z'] * ['0'])
    nums.extend(d['X'] * ['6'])
    nums.extend(d['G'] * ['8'])
    nums.extend(d['U'] * ['4'])
    nums.extend(d['W'] * ['2'])
    n5 = d['F'] - d['U']
    nums.extend(n5 * ['5'])
    n7 = d['V'] - n5
    nums.extend(n7 * ['7'])
    n3 = d['H'] - d['G']
    nums.extend(n3 * ['3'])
    n9 = d['I'] - d['X'] - d['G'] - n5
    #print d['I'], d['G'], n5
    nums.extend(n9 * ['9'])
    n1 = d['O'] - d['Z'] - d['W'] - d['U']
    nums.extend(n1 * ['1'])
    nums.sort()
    return ''.join(nums)

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        S = raw_input()
        res = solve(S)
        print 'Case #%d: %s' % (int(i), res)

if __name__ == '__main__':
    main()