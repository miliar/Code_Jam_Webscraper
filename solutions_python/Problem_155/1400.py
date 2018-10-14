cases = int(input())
for case in range(cases):
    shyness_max, shyness = input().split()
    total = 0
    additional = 0
    for required, amount in enumerate(shyness):
        amount = int(amount)
        if total < required:
            additional += required - total
            total += required - total
        total += amount
    print("Case #{}: {}".format(case+1, additional))