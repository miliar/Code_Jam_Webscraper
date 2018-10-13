__author__ = 'unknow'

def magic(case):
    c,f,x = allInput.readline().replace("\n", "").split(" ")
    c = float(c)
    f = float(f)
    x = float(x)
    result_list = []
    temp = []
    if c/2.0 > x:
        result = x/2.0
        print "Case #%d: %.7f" % (case, result)
        return

    for i in range(50000):
        speed = (f * i) + 2.0
        second = x / speed
        temp.append(c/speed)
        result_list.append(sum(temp[:-1]) + second)
        if i > 0:
            if result_list[i-1] < result_list[i]:
                print "Case #%d: %.7f" % (case, result_list[i-1])
                break

if __name__ == "__main__":
    allInput = open("B-small-attempt0.in", 'r')
    number_of_test_case = int(allInput.readline())
    case = 0
    if number_of_test_case > 100 or number_of_test_case < 1:
        exit(1)
    for a in range(number_of_test_case):
        case = case + 1
        magic(case)
    allInput.close()