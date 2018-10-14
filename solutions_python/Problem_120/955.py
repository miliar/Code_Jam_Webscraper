import sys
import math

# Paint required for n rings: 2 * n * r + 2 * n**2 - n
# Need to make n as large as possible, and paint required not exceed t

def solve(instream):
    center_radius, paint_amount = [float(x) for x in instream.readline().strip().split(" ")]
    a = 2.0
    b = 2 * center_radius - 1
    c = -paint_amount


    n = ((-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a))

    result = int(math.floor(n))

    # DIRTY HACK
    while True:
        required = 2 * result ** 2 + 2 * result * center_radius - result
        if required > paint_amount:
            result -= 1
        else:
            break

    return result


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
