"""
Google Code Jam, Problem ?
"""

def map_servings(proportion, amount):
    serving = 1
    all_servings = set()
    while True:

        if amount < proportion*serving*0.9:
            break

        if proportion*serving*0.9 <= amount and amount <= proportion*serving*1.1:
            all_servings.add(serving)
        serving += 1
    return all_servings


def find_smallest(list_of_sets, value):
    matches = [ s for s in  list_of_sets if value in s]
    if matches:
        matches.sort(key=min)
        return matches[0]
    else:
        return set()


def solve(ingredient_proportions, ingredients):
    """
    solve problem
    """
    servings = [list(map(lambda x: map_servings(proportion, x), packages)) \
                    for proportion, packages in zip(ingredient_proportions, ingredients)]
    
    
    sizes = set()
    for i in servings:
        for j in i:
            sizes.update(j)
            
    kits = 0
    for s in sizes:
        while True:
            # for each size find the smallest set containing 
            matches = [find_smallest(l, s) for l in servings]
            if all(matches):
                kits += 1
                for x, y in zip(matches, servings):
                    y.remove(x)
            else:
                break

    return kits
    # kits = 0
    # print(ingredient_proportions)
    # print(ingredients)
    # print(servings)

    # for s in sizes:
    #     while True:
    #         if all([s in l for l in servings]):
    #             for l in servings:
    #                 l.remove(s)
    #             kits += 1
    #         else:
    #             break
    
    # print(kits)

    #create an iterator for each list
    # positions = [iter(s) for s in servings]

    # while any(positions):
    #     for i in positions:
    #         i


def main():
    """
    main function
    """

    cases = int(input())
    for i in range(0, cases):
        size = list(map(int, input().split(' ')))
        ingredientCount = size[0]
        packageCount = size[1]

        ingredient_proportions = list(map(int, input().split(' ')))

        ingredients = []

        for _ in range(ingredientCount):
            ingredients.append(list(map(int, input().split(' '))))



        result = solve(ingredient_proportions, ingredients)

        print("Case #" + str(i+1) + ": " + str(result))

if __name__ == '__main__':
    main()
