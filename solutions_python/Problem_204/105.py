import sys
import math

def process():
    t = int(input())
    for i in range(1, t + 1):
        n_ingredients, n_packages = [int(s) for s in input().split(" ")]
        recipe = [int(s) for s in input().split(" ")]
        ingredient_rows = []
        for k in range(n_ingredients):
            r = [int(s) for s in input().split(" ")]
            ingredient_rows.append(r)

        package_tally = tally_valid_packages(recipe, ingredient_rows)
        print("Case #{}: {}".format(i, package_tally))





def tally_valid_packages(recipe, ingredient_rows):
    packages_to_make = []
    for i, row in enumerate(ingredient_rows):
        packages_to_make.append(sorted([r/recipe[i] for r in row]))

    #print(packages_to_make)
    tally = 0
    for val in packages_to_make[0]:
        package = [val]
        for i in range(1,len(packages_to_make)):
            for gred in packages_to_make[i]:
                test = package + [gred]
                #print(test)
                if package_is_valid(test):
                    package = test
                    break

        if len(package) == len(recipe) and package_is_valid(package):
            tally += 1
            for k in range(1, len(packages_to_make)):
                for e in packages_to_make[k]:
                    if e == package[k]:
                        packages_to_make[k].remove(e)
                        break

    return tally

def package_is_valid(kit):
    smallest = min(kit)
    largest = max(kit)
    return math.floor(smallest/.9) >= math.ceil(largest/1.1)



def get_servings_for_package(recipe, current_package):
    min_recipe = [.9*r for r in recipe]

    min_multiplier = sys.maxsize
    for i in range(len(recipe)):
        d = current_package[i] // min_recipe[i]
        if within_range(current_package[i], d*recipe[i]) and 0 < d < min_multiplier:
            min_multiplier = d

    target_package = [min_multiplier*i for i in recipe]
    print(target_package)
    okay = False
    while not okay:
        within_count = 0
        all_within = True
        for i in range(len(recipe)):
            if not within_range(current_package[i], target_package[i]):
                all_within = False
            else:
                within_count += 1
        if all_within:
            return 1 #doesn't matter

        if within_count == 0:
            return 0

        for i in range(len(target_package)):
            target_package[i] += recipe[i]


def within_range(actual, target):
    return actual >= target*0.9 and actual <= target*1.1

if __name__ == "__main__":
    process()
