import sys

def getBestTidyNum(num_str):
    num_int = int(num_str)
        
    while num_int > 0:
        isTidy = True
        size = len(num_str)
        for i in range(size - 1):
            if num_str[i] > num_str[i + 1]:
                isTidy = False
                break
        if isTidy:
            return num_str
        num_int = int(num_str)
        num_int = num_int - 1
        num_str = str(num_int)
       
    # this would return 0
    return str(num_int)
    
            




if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 2:
        print "usage:%s ip_file_name" % (sys.argv[0])
        exit(0)
    # read input file and store all inputs
    filename = sys.argv[1]
    with open(filename, "r") as file:
        data = file.readlines()
    caseNum = 0
    for line in data[1:]:
        print "Case #" + str(caseNum + 1) + ": " + getBestTidyNum(line.strip('\n'))
        caseNum = caseNum + 1
