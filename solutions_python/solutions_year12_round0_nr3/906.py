import sys

verbosity = False

def readStdinput_list(limit_input=False, multiplier=1, do_strip=True):
    input_list = []
    while 1:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break
        line = line if not do_strip else line.strip()
        input_list.append(line)
        if limit_input:
            if len(input_list) > 1:
                if int(input_list[0])*multiplier < (len(input_list)):
                    break
    return input_list

def readFile(in_file,limit_input=False, multiplier=1):
    input_list = []
    with open(in_file) as f:
        for line in f:
            line = line.rstrip("\r\n")
            input_list.append(line)
            if limit_input:
                if len(input_list) > 1:
                    if int(input_list[0])*multiplier < (len(input_list)):
                        break
    return input_list

def debug(msg):
    if verbosity:
        print str(msg)

def decide_verbosity(argn=2):
    global verbosity
    if len(sys.argv)>argn:
        if sys.argv[argn] in ["--v", "v", "verbose", "-verbose"]:
            verbosity = True

