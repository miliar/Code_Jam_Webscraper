import math

__author__ = 'ben'

lines = [line.rstrip('\n') for line in open('input')][1:]

outFile = open("output", "w")


def get_legit(l, n):
    for ind, i in enumerate(l):
        if n in i:
            return ind
    else:
        return -1

c = 1
parsing = 0
recipe = []
ingredients = []
ing = 0
max_ing = 0
for line in lines:
    if parsing == 0:
        parsing = 1
        max_ing = int(line.split(" ")[0])
        continue
    if parsing == 1:
        for i in line.split(" "):
            recipe.append(int(i))
        parsing = 2
        continue
    if parsing == 2:
        ingredients.append([])
        for i in line.split(" "):
            ingredients[ing].append(int(i))
        ing += 1
    if ing == max_ing:

        for ind, ing in enumerate(recipe):
            for i2, i in enumerate(ingredients[ind]):
                ingredients[ind][i2] /= ing
            ingredients[ind] = sorted(ingredients[ind])

        for i1, ingredient in enumerate(ingredients):
            for i2, i in enumerate(ingredient):
                largest = i / 0.9
                smallest = i / 1.1
                int_packages = range(math.ceil(smallest), math.floor(largest) + 1)
                ingredients[i1][i2] = int_packages

        number = 0
        indexes = [0] * len(ingredients)
        for j in range(1, int(1000000)):
            legit = True
            for ind, ingredient in enumerate(ingredients):
                if get_legit(ingredient, j) == -1:
                    legit = False
            while legit:
                for ind, ingredient in enumerate(ingredients):
                    ingredients[ind][get_legit(ingredient, j)] = range(-1000, -1000)
                for ind, ingredient in enumerate(ingredients):
                    if get_legit(ingredient, j) == -1:
                        legit = False
                number += 1

        parsing = 0
        recipe = []
        ingredients = []
        ing = 0
        max_ing = 0

        outFile.write("Case #{}: {}\n".format(c, number))
        number = 0
        c += 1
