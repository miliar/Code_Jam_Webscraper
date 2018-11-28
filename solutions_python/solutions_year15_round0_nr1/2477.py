import sys

def standing_ovation(shyness):
    total = 0
    add = 0
    for i,c in enumerate(shyness):
        if i > 0 and c > 0 and i > total:
            diff = i - total
            add += diff
            total += diff
        total += c
    return add


if __name__ == "__main__":
    output_file = open("%s.%s"%(sys.argv[1].split(".")[0],"out"),"w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        line = input_file.readline().strip().split()[1]
        shyness = map(int, line)
        result = standing_ovation(shyness)
        output_file.write("Case #%s: %s\n"%(i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
