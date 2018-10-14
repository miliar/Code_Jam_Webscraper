import sys

def main(argv):
    with open(argv[1], 'w') as outfile:
        with open(argv[0], 'r') as infile:
            T = int(infile.readline())
            for case in range(T):
                (A, B) = infile.readline().split()
                result = count_recycled_pairs(int(A), int(B))
                outfile.write('Case #%i: %i\n' % (case + 1, result))

def count_recycled_pairs(A, B):
    pairs = 0
    for i in range(A, B):
        permutations = get_permutaions(i)
        for p in permutations:
            if p > i and p <= B:
                pairs += 1
    return pairs


def get_permutaions(n):
    p = set()
    l = len(str(n))
    s = str(n) + str(n)   
    for i in range(1, l):
        p.add(int(s[i:i + l]))
    return p
    
if __name__ == '__main__':
    main(sys.argv[1:])
