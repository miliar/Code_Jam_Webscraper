def parse_pattern(line):
    pattern = []
    token = pattern
    for char in line:
        if char == '(':
            token = []
        elif char == ')':
            pattern.append(''.join(token))
            token = pattern
        else:
            token.append(char)
    return pattern

def make_tree(words):
    root = {}
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, {})
    return root

def solve(pattern, tree, i=0):
    if i >= len(pattern):
        return 1
    return sum(solve(pattern, tree[c], i + 1) for c in pattern[i] if c in tree)

def main():
    L, D, N = map(int, raw_input().split())
    tree = make_tree(raw_input() for _ in xrange(D))
    for case in xrange(N):
        pattern = parse_pattern(raw_input())
        print 'Case #%d: %d' % (case + 1, solve(pattern, tree))

if __name__ == '__main__':
    main()
