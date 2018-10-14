import fileinput 
import sys
import math

stdin = fileinput.input()
debug = False

def sort(R, Y, B):
    choices = [ (R, 'R'), (Y, 'Y'), (B, 'B') ]
    choices = list(reversed(sorted(choices)))
    return choices

def assert_is_valid(s):
    for i in range(len(s)):
        assert(s[i] != s[(i + 1) % len(s)])

def do_case(N, R, O, Y, G, B, V):
    assert(O == 0);
    assert(G == 0);
    assert(V == 0);
    [ (biggest, biggest_color), (middle, middle_color), (smallest, smallest_color) ] = sort(R, Y, B)
    # If > 1/2 horses have one color then impossible
    if biggest > middle + smallest: 
        print "N/2: ", float(N)/2
        return "IMPOSSIBLE"
    y = (biggest - middle)
    x = y * [ biggest_color, middle_color, biggest_color, smallest_color ]
    biggest -= 2 * y
    middle -= y
    smallest -= y
    y = middle - smallest
    x += y * [ biggest_color, middle_color ]
    biggest -= y
    middle -= y
    x += smallest * [ biggest_color, middle_color, smallest_color ]
    s = ''.join(x)
    assert_is_valid(s)
    return s

T = int(next(stdin))
print "T:", T

for case_num in range(1, T+1):
    case_input = next(stdin)
    [N, R, O, Y, G, B, V] = [ int(x) for x in case_input.split(' ') ]
    print "(N, R, O, Y, G, B, V):", (N, R, O, Y, G, B, V)
    assert(R+ O+ Y+ G+ B+ V == N);
    x = do_case(N, R, O, Y, G, B, V)
    print "Case #{}: {}".format(case_num, x)
    sys.stdout.flush()

