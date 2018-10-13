import math
"""
a = [1]
try:
    index_value = a.index(44)
except ValueError:
    index_value = -1



    #goalIngre = input().split(" ")
    #goalIngre = [int(x) for x in goalIngre]
    #floor = math.ceil(ingredient / goalIngre[p] / 1.1)
    #ceil = math.floor(ingredient / goalIngre[p] / 0.9)

"""

t = int(input())  # read a line with a single integer
F = open("problem1-result.in", 'w')
for i in range(1, t+ 1):
    total, num_cake = input().split(" ")  # read a list of integers, 2 in this case
    total = int(total)
    num_cake = int(num_cake)
    cakes = []
    cake_rad = []
    cake_height = []
    cake_side = []
    for j in range(total):
        cake_info = input().split(" ")
        cake_info = [int(x) for x in cake_info]
        cakes.append(cake_info)
        cake_rad.append(cake_info[0])
        #cake_height.append(cake_info[1])
        #cake_side.append(cake_info[0] * cake_info[1])


    syrup = []

    for k in range(total -num_cake + 1):
        cakes.sort(key=lambda x: -x[0])
        big_cake = cakes.pop(0)
        max_rad = big_cake[0]
        cakes.sort(key=lambda x: -2*math.pi*x[0]*x[1])

        surface = math.pi * (max_rad ** 2) + 2 * math.pi * big_cake[0] * big_cake[1]
        for k in range(num_cake - 1):
            side_surface = 2 * math.pi * cakes[k][0] * cakes[k][1]
            surface += side_surface
        syrup.append(surface)



    best_surface = max(syrup)







    print("Case #{}: {}\n".format(i, best_surface))
    F.write("Case #{}: {}\n".format(i, best_surface))

F.close()