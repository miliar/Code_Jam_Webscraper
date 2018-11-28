input = "C-small-attempt1.in"

multiply = dict()

multiply["1"] = dict()
multiply["i"] = dict()
multiply["j"] = dict()
multiply["k"] = dict()
multiply["-1"] = dict()
multiply["-i"] = dict()
multiply["-j"] = dict()
multiply["-k"] = dict()

multiply["1"]["1"] = "1"
multiply["1"]["i"] = "i"
multiply["1"]["j"] = "j"
multiply["1"]["k"] = "k"

multiply["i"]["1"] = "i"
multiply["i"]["i"] = "-1"
multiply["i"]["j"] = "k"
multiply["i"]["k"] = "-j"

multiply["j"]["1"] = "j"
multiply["j"]["i"] = "-k"
multiply["j"]["j"] = "-1"
multiply["j"]["k"] = "i"

multiply["k"]["1"] = "k"
multiply["k"]["i"] = "j"
multiply["k"]["j"] = "-i"
multiply["k"]["k"] = "-1"

multiply["-1"]["1"] = "-1"
multiply["-1"]["i"] = "-i"
multiply["-1"]["j"] = "-j"
multiply["-1"]["k"] = "-k"

multiply["-i"]["1"] = "-i"
multiply["-i"]["i"] = "1"
multiply["-i"]["j"] = "-k"
multiply["-i"]["k"] = "j"

multiply["-j"]["1"] = "-j"
multiply["-j"]["i"] = "k"
multiply["-j"]["j"] = "1"
multiply["-j"]["k"] = "-i"

multiply["-k"]["1"] = "-k"
multiply["-k"]["i"] = "-j"
multiply["-k"]["j"] = "i"
multiply["-k"]["k"] = "1"


def reduce(a):
    if not a:
        return False
    if a[0] == "-":
        accu = "-1"
        a = a[1:]
    else:
        accu = "1"
    for x in a:
        accu = multiply[accu][x]
    return accu == "-1"


def reduce_to_i(a):
    if a[0] == "-":
        accu = "-1"
        a = a[1:]
    else:
        accu = "1"
    for x in xrange(len(a)):
        accu = multiply[accu][a[x]]
        if accu == "i":
            if reduce_to_j(a[x+1:]):
                return True
    return False


def reduce_to_j(a):
    if not a:
        return False
    if a[0] == "-":
        accu = "-1"
        a = a[1:]
    else:
        accu = "1"
    for x in xrange(len(a)):
        accu = multiply[accu][a[x]]
        if accu == "j":
            if reduce_to_k(a[x+1:]):
                return True
    return False


def reduce_to_k(a):
    if not a:
        return False
    if a[0] == "-":
        accu = "-1"
        a = a[1:]
    else:
        accu = "1"
    for x in a:
        accu = multiply[accu][x]
    return accu == "k"


with open(input, "r") as input_file:
    nb_case = int(input_file.readline())

    for count in xrange(nb_case):
        foo, nb = input_file.readline().strip().split()
        nb = int(nb)
        a = input_file.readline().strip() * nb
        if not reduce(a):
            print "Case #%d:" %(count+1), "NO"
        elif reduce_to_i(a):
            print "Case #%d:" %(count+1), "YES"
        else:
            print "Case #%d:" %(count+1), "NO"
