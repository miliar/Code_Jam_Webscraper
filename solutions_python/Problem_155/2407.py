import sys

def how_many_more(c):
    required = 0;
    for i in range(len(c) - 1, -1, -1):
        already_clapping = sum(c[:i])
        if already_clapping < i:
            required = max(required, i - already_clapping)
    return required

num_tests = int(sys.stdin.readline())
for index, test in enumerate(sys.stdin):
    max_shyness, nums = test.strip().split()
    audience = [ int(i) for i in nums ]
    print("Case #%d:" % (index+1), how_many_more(audience))
        
        
