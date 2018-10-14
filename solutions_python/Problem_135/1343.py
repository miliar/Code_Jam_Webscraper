import sys
def compare(row_1, row_2):
    intersection = set(row_1) & set(row_2)
    if len(intersection) == 0:
        return "Volunteer cheated!"
    if len(intersection) > 1:
        return "Bad magician!"
    return intersection.pop()

if __name__ == "__main__":
    output_file = open("%s.%s"%(sys.argv[1].split(".")[0],"out"),"w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        row_num_1 = int(input_file.readline())
        for j in xrange(row_num_1 - 1):
            input_file.readline()
        row_1 = input_file.readline().strip().split(" ")
        #print "row 1", row_1
        #skip remainder
        for j in xrange(4 - row_num_1):
            input_file.readline()
        row_num_2 = int(input_file.readline())
        for j in xrange(row_num_2 - 1):
            input_file.readline()
        row_2 = input_file.readline().strip().split(" ")
        #print "row 2", row_2
        for j in xrange(4 - row_num_2):
            input_file.readline()
        result = compare(row_1, row_2)
        output_file.write("Case #%s: %s\n"%(i+1, result))
    output_file.close()
    input_file.close()
    print "Done!"