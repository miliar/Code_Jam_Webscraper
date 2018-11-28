import math


def sol_print(value):
    sol_print.line_number += 1
    print "Case #%d: %s"%(sol_print.line_number, value)


def compute_surface_of_pk(R):
    surface = float(float(math.pi) * float(R) * float(R))
    return surface


def compute_side_surface_of_pk(R, H):
    # formula: 2 * II * r = perimeter, perimter * H = side_surface
    side_surface = float(float(2) * float(math.pi) * float(R) * float(H))
    return side_surface


def compute_total_surface(s1, s2):
    return float(s1 + s2)


def resolve(N, K, pancakes):
    for pancake in pancakes:
        pancake.append(compute_side_surface_of_pk(pancake[0], pancake[1]))
        pancake.append(compute_surface_of_pk(pancake[0]))
        pancake.append(compute_total_surface(pancake[2], pancake[3]))
    pancakes = sorted(pancakes, key=lambda x: x[0], reverse=True)
    pancakes = sorted(pancakes, key=lambda x: x[4], reverse=True)

    fst_pancake = pancakes.pop(0)
    pancakes = sorted(pancakes, key=lambda x: x[2], reverse=True)
    k_pk = pancakes[:K - 1]
    k_pk.append(fst_pancake)
    sol = 0
    max_surface = 0
    for pk in k_pk:
        sol += pk[2]
        max_surface = max(max_surface, pk[3])
    sol += max_surface
    return "%.9f" % sol


def main():
    sol_print.line_number = 0
    nb_test_cases = int(raw_input())

    for idx, test_case in enumerate(range(nb_test_cases)):
        input = str(raw_input())
        N, K = map(int, input.split())
        pancakes = []
        for pancake in range(N):
            h_input = str(raw_input())
            R, H = map(int, h_input.split())
            pancakes.append([R, H])
        sol = resolve(N, K, pancakes)
        sol_print(sol)

if __name__ == "__main__":
    main()
