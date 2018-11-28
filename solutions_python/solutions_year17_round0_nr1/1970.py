import sys,os


def read_input(filename):
    f = open(filename)
    lines = f.readlines()
    curentLine = 0
    _T = int(lines[curentLine])
    for T in range(_T):
        curentLine +=1
        lista = lines[curentLine].split()
        response = solver(lista[0], int(lista[1]))
        print("Case #%d: %s" % (T+1, response))
    f.close()

def all_pancakes_up(string):
    if string == None:
        return False
    return True if '-' not in string else False

def reverse_pancakes(string, k, starting):
    """
    :param string: 
    :param k: 
    :param starting: indice, incepe de la 0
    :return: 
    """
    if (len(string) < k + starting):
        # print("EROARE: nu pot sa fac reverse !!!")
        return None
    lstring = list(string)
    for i in range(k):
        if lstring[starting + i] == '+':
            lstring[starting + i] = '-'
        else:
            lstring[starting + i] = '+'
    # print("DEBUG: ", lstring)
    string = "".join(lstring)

    return string


def solver(string, k):
    flipnr = 0
    starting_char = 0

    while not all_pancakes_up(string):
        if string[starting_char] == '+':
            starting_char += 1
            continue
        string = reverse_pancakes(string, k, starting_char)
        if string is None: # in acest punct inseamna ca nu mai pot intoarce ultimele goafre
            break
        flipnr += 1

    if all_pancakes_up(string):
        return str(flipnr)
    else:
        return 'IMPOSSIBLE'

if len(sys.argv)>1 and sys.argv[1]:
    inputFile = sys.argv[1]
else:
    inputFile = "test_input.txt"

read_input(inputFile)
