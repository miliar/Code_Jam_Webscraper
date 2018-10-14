# it was so funny that I had to try it in the dumbest possible way

import sys, string

input_f = open(sys.argv[1],'r')
nb_cases = string.atoi(input_f.readline().rstrip('\n'))

for i in range(0, nb_cases):
    dict = {"w":0,"we":0,"wel":0,"welc":0,"welco":0,"welcom":0,\
            "welcome":0,"welcome ":0,"welcome t":0,"welcome to":0,"welcome to":0,\
            "welcome to ":0,"welcome to c":0,"welcome to co":0,"welcome to cod":0,\
            "welcome to code":0,"welcome to code ":0,"welcome to code j":0,\
            "welcome to code ja":0,"welcome to code jam":0}
    for c in input_f.readline().rstrip('\n'):
        if c == 'w':
            dict["w"] += 1
        elif c == ' ':
            dict["welcome "] += dict["welcome"]
            dict["welcome to "] += dict["welcome to"]
            dict["welcome to code "] += dict["welcome to code"]
        elif c == 'e':
            dict["we"] += dict["w"]
            dict["welcome"] += dict["welcom"]
            dict["welcome to code"] += dict["welcome to cod"]
        elif c == 'l':
            dict["wel"] += dict["we"]
        elif c == 'c':
            dict["welc"] += dict["wel"]
            dict["welcome to c"] += dict["welcome to "]
        elif c == 'o':
            dict["welco"] += dict["welc"]
            dict["welcome to"] += dict["welcome t"]
            dict["welcome to co"] += dict["welcome to c"]
        elif c == 'm':
            dict["welcom"] += dict["welco"]
            dict["welcome to code jam"] += \
                    dict["welcome to code ja"]
        elif c == 't':
            dict["welcome t"] += dict["welcome "]
        elif c == 'd':
            dict["welcome to cod"] += dict["welcome to co"]
        elif c == 'j':
            dict["welcome to code j"] += \
                    dict["welcome to code "]
        elif c == 'a':
            dict["welcome to code ja"] += \
                    dict["welcome to code j"]

    result = str(dict["welcome to code jam"])
    while len(result) < 4:
        result = '0' + result
    print "Case #" + str(i+1) + ": " + result
