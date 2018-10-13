import sys

def check_case(file_):
    row1 = int(file_.next().strip("\n"))
    set1 = set()
    for i in xrange(1, 5):
       data = file_.next().strip("\n")
       if row1 == i:
           set1 = set(data.split(" "))

    row2 = int(file_.next().strip("\n"))
    set2 = set()
    for i in xrange(1, 5):
        data = file_.next().strip("\n")
        if row2 == i:
            set2 = set(data.split(" "))

    return list(set1.intersection(set2))


def main(argv):
    with open(argv[1]) as file_:
        count = int(file_.next().strip("\n"))
        for i in xrange(count):
            result = check_case(file_)
            if len(result) == 0:
                result = "Volunteer cheated!"
            elif len(result) == 1:
                result = result[0]
            else:
                result = "Bad magician!"
            print "Case #{num}: {result}".format(num=i+1, result=result)


if __name__ == '__main__':
    main(sys.argv)
