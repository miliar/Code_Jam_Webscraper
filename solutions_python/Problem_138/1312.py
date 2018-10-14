import sys

inp = sys.stdin
get_int = lambda: int(inp.readline())
get_floats = lambda: map(float, inp.readline().split())

T = get_int()
for case_number in range(1, T + 1):
    N = get_int()
    naomi_blocks = sorted(get_floats())
    ken_blocks = sorted(get_floats())
    ken_blocks1 = list(ken_blocks)
    assert len(naomi_blocks) == len(ken_blocks) == N
    war = d_war = 0
    for n in reversed(naomi_blocks):
        if n > ken_blocks[-1]:
            ken_blocks.pop(0)
            war += 1
        else:
            for i, k in enumerate(ken_blocks):
                if k > n:
                    ken_blocks.pop(i)
                    break
    ken_blocks = ken_blocks1
    for n in naomi_blocks:
        if n < ken_blocks[0]:
            ken_blocks.pop()
        else:
            ken_blocks.pop(0)
            d_war += 1
    print 'Case #%d: %d %d' % (case_number, d_war, war)

