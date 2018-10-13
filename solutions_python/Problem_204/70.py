def solve(n, p, recipe, ingredients):
    kits = 0
    for ingredient in ingredients:
        ingredient.sort()

    # Attempt to make progressively larger kits until an ingredient runs out
    servings = 0
    while True:
        for i, ingredient in enumerate(ingredients):
            # minimum size kit that could be made with this ingredient
            servings = max(servings, (ingredient[0] * 10 + recipe[i]*11 - 1) // (recipe[i]*11) )

        max_kits_of_this_size = 1000000
        for i, ingredient in enumerate(ingredients):
            # For each ingredient:
            # Count the number of smaller, and the amount of correct packages
            smaller = 0
            correct_size = 0
            for package in ingredient:
                if package * 10 < recipe[i] * servings * 9:
                    smaller += 1
                elif package * 10 > recipe[i] * servings * 11:
                    break
                else:
                    correct_size += 1
            # Remove the too small packages
            ingredients[i] = ingredient[smaller:]

            # Set the limiting number of kits of this size
            max_kits_of_this_size = min(max_kits_of_this_size, correct_size)

        # Add the kits made of this size, and remove the ingredients used
        kits += max_kits_of_this_size
        for i, ingredient in enumerate(ingredients):
            ingredients[i] = ingredient[max_kits_of_this_size:]

        # Done when any ingredient runs out
        for ingredient in ingredients:
            if len(ingredient) == 0:
                return kits


input()
case = 0
while True:
    case += 1
    try:
        n, p = map(int, input().split(' '))
        recipe = list(map(int, input().split(' ')))
        ingredients = []
        for i in range(n):
            ingredients.append(list(map(int, input().split(' '))))
    except:
        break
    print('Case #{}: {}'.format(case, solve(n, p, recipe, ingredients)))

