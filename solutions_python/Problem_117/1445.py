__author__ = 'Ruben'


def check(lawn):
    for y in xrange(rows):
        for x in xrange(cols):
            target_height = lawn[y][x]
            #print "@"+str(x),",", y, "=", target_height



            #print target_height,

            #try top ray
            #print "try top"
            top_bad = False
            ray_x = x
            for ray_y in xrange(rows):
                if lawn[ray_y][ray_x] > target_height:
                    top_bad = True
                    #print ray_x,",", ray_y

            #try left ray
            ##print "try left"
            left_bad = False
            ray_y = y
            for ray_x in xrange(cols):
                if lawn[ray_y][ray_x] > target_height:
                    left_bad = True
                    #print ray_x,",", ray_y

            if top_bad and left_bad:
                return False

    return True

file = open("B-small-attempt1.in")
#file = open("qual_02.txt")

cases = int(file.readline().strip())

for c in xrange(cases):
    tmp = file.readline().strip().split(" ")
    rows = int(tmp[0])
    cols = int(tmp[1])

    c += 1

    lawn = []
    for i in xrange(rows):
        lawn += [file.readline().strip().split(" ")]

    #for row in lawn:
    #    print "".join(row)

    if check(lawn):
        print "Case #" + str(c) + ": YES"
    else:
        print "Case #" + str(c) + ": NO"





