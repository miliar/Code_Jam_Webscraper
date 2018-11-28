import sys,os


def read_input(filename):
    f = open(filename)
    lines = f.readlines()
    curentLine = 0
    _T = int(lines[curentLine])
    for T in range(_T):
        curentLine +=1
        nr_string = lines[curentLine].strip()
        response = solver(nr_string)
        print("Case #%d: %s" % (T+1, response))
    f.close()

def tidy_nr(nr_string):
    """
    Return: o tupla care contine
                True / False : daca e tidy sau nu
                pozitia in string (incepe de la indexul 0) a cifrei care nu mail respecta regula
    """
    length = len(nr_string)

    if length == 1:  # shorcut : 0->9 are tidy
        return True, 0
    if nr_string[length-1] == '0':  # shorcut : any number ending '0' is not tidy
        return False, length-1

    for i in range(length-1):
        if nr_string[i] > nr_string[i+1]:
            return False, i+1

    return True, 0

def generate_tidy_nr(nr_string):
    nr_list = list(nr_string)
    is_tidy, index_non_tidy = tidy_nr(nr_string)

    while not is_tidy:
        if index_non_tidy < 1:
            raise ValueError

        new_nr = int(nr_list[index_non_tidy-1]) - 1
        nr_list[index_non_tidy-1] = str(new_nr)
        for i in range(index_non_tidy, len(nr_list)):
            nr_list[i] = '9'

        # print("DEBUG ", nr_list)
        nr_string = "".join(nr_list)

        is_tidy, index_non_tidy = tidy_nr(nr_string)

    return nr_string.lstrip('0')

def solver(nr_string):
    tidy, index_non_tidy = tidy_nr(nr_string)

    if tidy:  # shortcut
        return nr_string
    else:  # get the previous tidy number
        return generate_tidy_nr(nr_string)



if len(sys.argv)>1 and sys.argv[1]:
    inputFile = sys.argv[1]
else:
    inputFile = "test_input.txt"

read_input(inputFile)
