num_cases = int(input())
for z in range(num_cases):
    row1 = int(input())
    table = {}
    table[1] = input().split(' ')
    table[2] = input().split(' ')
    table[3] = input().split(' ')
    table[4] = input().split(' ')
    numbers = table[row1]
    row2 = int(input())
    table = {}
    table[1] = input().split(' ')
    table[2] = input().split(' ')
    table[3] = input().split(' ')
    table[4] = input().split(' ')
    final_numbers = []
    for x in table[row2]:
        if x in numbers:
            final_numbers.append(x)
    if len(final_numbers) == 1:
        print("Case #%d: %s" % ((z+1), final_numbers[0]))
    elif len(final_numbers) > 1:
        print("Case #%d: Bad magician!" % (z+1))
    else :
        print("Case #%d: Volunteer cheated!" % (z+1))


# table1 = {}
# table2 = {}
# row1 = {}
# row2 = {}
# num_cases = int(input())
# for z in range(num_cases):
#     row1[z] = int(input())
#     table1[z] = {}
#     table1[z][1] = input().split(' ')
#     table1[z][2] = input().split(' ')
#     table1[z][3] = input().split(' ')
#     table1[z][4] = input().split(' ')
