__author__ = 'trisch'

if __name__ == "__main__":

    filename = "A-large.in"
    number = 0
    case = 0
    with open("output_large.txt", "w") as f:
        for line in open(filename):
            if not number:
                number = int(line.strip())
            else:
                smax, numbers = line.strip().split()
                standing_persons = 0
                invited = 0
                for ind, person in enumerate(numbers):
                    if standing_persons < ind:
                        invited += 1
                        standing_persons += 1
                    standing_persons += int(person)
                f.write("Case #{0}: {1}\n".format(case + 1, invited))
                print "Case #{0}: {1}".format(case + 1, invited)
                case += 1
