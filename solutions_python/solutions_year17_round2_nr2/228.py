def solve(n, r, o, y, g, b, v):
    top = max(r, y, b)
    bottom = min(r, y, b)
    mid = r + y + b - top - bottom

    if top > mid + bottom:
        return "IMPOSSIBLE"

    top_orig = top
    mid_orig = mid
    bottom_orig = bottom

    result = ""

    tb = top - mid
    for i in xrange(0, tb):
        result = result + "TZ"
    top = top - tb
    bottom = bottom - tb
    for i in xrange(0, bottom):
        result = result + "TMZ"
    top = top - bottom
    mid = mid - bottom
    for i in xrange(0, top):
        result = result + "TM"

    if top_orig == r:
        result = result.replace("T", "R")
        if mid_orig == y:
            result = result.replace("M", "Y")
            result = result.replace("Z", "B")
        elif mid_orig == b:
            result = result.replace("M", "B")
            result = result.replace("Z", "Y")
    elif top_orig == y:
        result = result.replace("T", "Y")
        if mid_orig == b:
            result = result.replace("M", "B")
            result = result.replace("Z", "R")
        elif mid_orig == r:
            result = result.replace("M", "R")
            result = result.replace("Z", "B")
    elif top_orig == b:
        result = result.replace("T", "B")
        if mid_orig == y:
            result = result.replace("M", "Y")
            result = result.replace("Z", "R")
        elif mid_orig == r:
            result = result.replace("M", "R")
            result = result.replace("Z", "Y")
            
    return result

t = int(raw_input())
for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(x) for x in raw_input().split(" ")]
    print "Case #{}: {}".format(i, solve(n, r, o, y, g, b, v))
