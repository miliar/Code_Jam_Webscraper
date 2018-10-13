import math

def get_level_number(K):
    return len(bin(K)[2:]) - 1

def get_max_min_of_width(width):
    if width % 2 == 0: # even
        return width/2, width/2 - 1
    dist = math.floor(width/2.0)
    return dist, dist

def get_min_max(intitial_width, K):
    level = get_level_number(K)
    if level == 0:
        return get_max_min_of_width(intitial_width)
    consumed_in_last_level = 2**(level) - 1
    left = intitial_width - consumed_in_last_level
    division_in_current = 2**level
    if left <= division_in_current:
        return 0, 0
    if K - consumed_in_last_level > left % division_in_current:
        return get_max_min_of_width(left / division_in_current)
    return get_max_min_of_width((left / division_in_current) + 1)


if __name__ == "__main__":
    n = int(raw_input())
    for i in range(0, n):
        inp = raw_input().strip().split(' ')
        N = int(inp[0])
        K = int(inp[1])
        min, max = get_min_max(N, K)
        print "Case #%d: %d %d" % ( i + 1, int(min), int(max))
