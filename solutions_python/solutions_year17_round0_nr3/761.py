# Guillermo Ortas

# dataFile = open("C-small-2-attempt0.in", 'r')
dataFile = open("C-large.in", 'r')

# dataFile = open("test.txt", 'r')
target = open('output_L.out', 'w+')

entries = dataFile.readline()

def add_son(son, num, vals_l, vals_count_l):
    if son not in vals_l:
        vals_l.append(son)
        vals_count_l.append(num)
    else:
        vals_count_l[vals_l.index(son)] += num
    return vals_l, vals_count_l

# def add_son(son, num):
#     if son not in vals:
#         vals.append(son)
#         vals_count.append(num)
#     else:
#         vals_count[vals.index(son1)] += num
#     return 1

m = 1
for line in dataFile:
    stalls = int(line.split(" ")[0])
    people = int(line.split(" ")[1])

    vals = [stalls]
    vals_count = [1]

    max_vals = max(vals)
    max_vals_count = vals_count[vals.index(max_vals)]
    p = 0

    while p < people and max_vals > 0:  # for each person, stop when done
        # print str(m) + " " + str(p)
        max_vals = max(vals)
        max_vals_count = vals_count[vals.index(max_vals)]
        vals.remove(max_vals)
        vals_count.remove(max_vals_count)
        if max_vals % 2 == 0:  # if even, two sons
            son1 = max_vals/2
            son2 = max_vals/2-1
            # add_son(son1, max_vals)
            # add_son(son2, max_vals)
            vals, vals_count = add_son(son1, max_vals_count, vals, vals_count)
            vals, vals_count = add_son(son2, max_vals_count, vals, vals_count)
        else:  # if odd, one son
            son1 = (max_vals-1)/2
            vals, vals_count = add_son(son1, 2*max_vals_count, vals, vals_count)
            # add_son(son1, 2*max_vals)
        p += max_vals_count
    # print str(vals) + " " + str(vals_count) + "\n"
    # print "Case #" + str(m) + ": "
    target.write("Case #" + str(m) + ": ")
    if max_vals % 2 == 0:  # if even, two sons
        son1 = max_vals/2
        son2 = max_vals/2-1
        target.write(str(son1) + " " + str(son2))
        # print son1, son2
    else:  # if odd, one son
        # print son1, son1
        target.write(str(son1) + " " + str(son1))
    target.write("\n")
    m += 1

target.close()

























# # dataFile = open("C-small-1-attempt0.in", 'r')
# dataFile = open("test.txt", 'r')
# target = open('output.out', 'w+')
#
# entries = dataFile.readline()
#
# people_lst = []
# stalls_lst = []
#
# for line in dataFile:
#     stalls_lst.append(int(line.split(" ")[0]))
#     people_lst.append(int(line.split(" ")[1]))
#
# for i in range(len(stalls_lst)):  # for each entry
#     stalls = stalls_lst[i]
#     people = people_lst[i]
#     sectors = [stalls]
#     for j in range(people):  # for each person
#         sector=max(sectors)
#         sectors.remove(sector)
#         if sector % 2 == 0:
#             sectors.append(sector/2)
#             sectors.append(sector/2-1)
#         else:
#             sectors.append((sector-1)/2)
#             sectors.append((sector-1)/2)
#     # print(max(sectors))
#     last_fringe = max(sectors)
#     print "Case #" + str(i+1) + ": "
#     target.write("Case #" + str(i+1) + ": ")
#     if sector == 0:
#         print str(sector) + " " + str(sector)
#         target.write(str(sector) + " " + str(sector))
#     else:
#         if sector % 2 == 0:
#             print str(sector / 2) + " " + str((sector / 2) - 1)
#             target.write(str(sector / 2) + " " + str((sector / 2) - 1))
#         else:
#             print str((sector - 1) / 2) + " " + str((sector - 1) / 2)
#             target.write(str((sector - 1) / 2) + " " + str((sector - 1) / 2))
#     target.write("\n")
#
# target.close()
