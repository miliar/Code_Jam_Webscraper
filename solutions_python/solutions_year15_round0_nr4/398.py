data = open("input/problemd.txt")
nb_cases = int(data.readline())

# ominos = []
#
# # 1-omino
# omino1 = []
# omino1.append([(0, 0)])
# ominos.append(omino1)
#
# # 2-omino
# omino2 = []
# omino2.append([(0, 0), (1, 0)])
# ominos.append(omino2)
#
# # 3-omino
# omino3 = []
# omino3.append([(0, 0), (1, 0), (2, 0)])
# omino3.append([(0, 0), (1, 0), (1, 1)])
# ominos.append(omino3)

# for i in xrange(1, len(ominos)):
#     omino = ominos[i]
#     to_add = []
#     for shape in omino:
#         print shape
#         new_shape = []
#         for deltaX, deltaY in shape:
#             new_shape.append((deltaY, deltaX))
#         print new_shape


for z in xrange(nb_cases):
    print "Case #%d:" % (z + 1),
    X, R, C = [int(x) for x in data.readline().split(" ")]

    # brute force
    if (R * C) % X != 0 or (R * C) < X:
        print "RICHARD"
        continue

    if X == 1:
        print "GABRIEL"

    if X == 2:
        print "GABRIEL"

    if X == 3:
        if R != 1 and C != 1:
            print "GABRIEL"
        else:
            print "RICHARD"

    if X == 4:
        if R == 1 or C == 1:
            print "RICHARD"
        elif R == 2 or C == 2:
            print "RICHARD"
        else: # 4x4
            print "GABRIEL"



