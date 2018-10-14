numbers = [1,4,9,121,484,10201,12321,14641,40804,44944,69696,94249,698896,1002001,1234321,4008004,5221225,6948496,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,522808225,617323716]

if __name__ == "__main__":
    
    T = int(raw_input())
    case = 0

    while T:
        cuenta = 0
        case += 1
        input = raw_input()
        A = int(input.split()[0])
        B = int(input.split()[1])

        for a in numbers:
            if a >= A and a <= B:
                cuenta = cuenta + 1
        print "Case #"+str(case)+": "+str(cuenta)
        T = T - 1
