import sys

def min_flips(test, k):
    count_flips = 0
    for i in range(len(test) - k + 1):
        if test[i] == 1:
            count_flips += 1
            for j in range(k):
                test[i + j] ^= 1
    if sum(test) == 0:
        return count_flips
    else:
        return 'IMPOSSIBLE'


def main(args):
    f = open('A-large.in', 'r')
    o = open('A-large.out', 'w')
    t = int(f.readline())
    for i in range(t):
        test, k = f.readline().strip().split()
        test = [0 if x == '+' else 1 for x in test]
        k = int(k)
        print('Case #{0}: {1}'.format(i+1, str(min_flips(test, k))), file=o)
    f.close()
    o.close()
            
            

if __name__ == '__main__':
    main(sys.argv)