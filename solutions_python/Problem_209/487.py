from sys import stdin
from math import pi as PI

def height_area(radius, height):
    return PI * 2 * radius * height

def radius_area(radius):
    return PI * radius * radius

def reorder_cakes(cakes, largest_radius):
    new_cake = []
    for cake in cakes:
        new_exposed_area = height_area(cake[2], cake[1])
        if cake[2] > largest_radius:
            new_exposed_area += radius_area(cake[2]) - radius_area(largest_radius)
        new_cake.append((new_exposed_area, cake[1], cake[2]))
    new_cake.sort(reverse=True)
    return new_cake

def solve_cakes(radii, heights, areas, serves):
    # First find the overall cake size
    cakes = list(zip(areas, heights, radii))
    cakes.sort(reverse=True)
    largest_radius = cakes[0][2]
    current_exposed_area = cakes[0][0]
    current_stack = 1
    cakes.pop(0)

    cakes = reorder_cakes(cakes, largest_radius)
    while(current_stack < serves):
        current_exposed_area += cakes[0][0]
        current_stack += 1
        need_reset = False
        if cakes[0][2] > largest_radius:
            largest_radius = cakes[0][2]
            need_reset = True
        cakes.pop(0)
        if need_reset:
            cakes = reorder_cakes(cakes, largest_radius)
    return current_exposed_area

def main():
    test_cases  = int(stdin.readline())
    for i in range(1, test_cases + 1):
        num_cakes, order = (int(z) for z in stdin.readline().split())
        radii = []
        heights = []
        areas = []
        for x in range(num_cakes):
            radius, height = (int(z) for z in stdin.readline().split())
            radii.append(radius)
            heights.append(height)
            areas.append(height_area(radius, height) + radius_area(radius))
        result = solve_cakes(radii, heights, areas, order)

        print("Case #%s: %10.8f" % (str(i), result))

main()
