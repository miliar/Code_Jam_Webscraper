lines = [line.strip() for line in open('A-small-attempt3.in')]

num_trials = int(lines.pop(0))

index = 0

while index < num_trials:
    first_index = int(lines.pop(0)) - 1
    first_row = lines[first_index]
    # Delete the first 4 rows
    del lines[0:4]

    second_index = int(lines.pop(0)) - 1
    second_row = lines[second_index]
    # Delete the next 4 rows
    del lines[0:4]

    items_first = set(first_row.split(" "))
    items_second = set(second_row.split(" "))

    in_both = list(items_first.intersection(items_second))

    if len(in_both) == 1:
        print "Case #{}: {}".format(index+1, in_both[0])
    elif len(in_both) > 1:
        print "Case #{}: Bad magician!".format(index+1)
    else:
        print "Case #{}: Volunteer cheated!".format(index+1)
    index += 1
