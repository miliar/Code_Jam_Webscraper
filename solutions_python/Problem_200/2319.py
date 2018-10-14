# GCJ - 02 #
# by meist3r-ed #

# DEFINE #
# ---------------------------------------------------------------------------- #
DEBUG = 0
# ---------------------------------------------------------------------------- #

# FUNCTIONS #
# ---------------------------------------------------------------------------- #
# Checks if "sol" is correct
def checkSolution(sol):
    out = str(sol)
    size = len(out)

    tmp = int(out[0])

    # See if there is any number that breaks the crescent
    for i in range(1, size):
        if(int(out[i]) < tmp):
            return 0
        else:
            tmp = int(out[i])

    return 1

# Calculates the solution for "out"
def calcSolution(out):
    out = str(out)
    out = list(out)
    size = len(out)

    tmp = int(out[0])
    lastvalid = tmp
    lastvalidindex = 0

    if(DEBUG): print("thinking...")

    # Finds the breaking point for calculus (last valid distinct number)
    for i in range(1, size):
        if(int(out[i]) < tmp):
            break
        else:
            tmp = int(out[i])
            if(lastvalid != tmp):
                lastvalid = tmp
                lastvalidindex = i

    # Decreases last valid number
    out[lastvalidindex] = int(out[lastvalidindex]) - 1

    # Every number beyond that = 9
    for j in range(lastvalidindex + 1, size):
        out[j] = 9

    # Assembles list back to string and to int
    for i in range(0, size):
        out[i] = str(out[i])
    out = ''.join(out)
    out = int(out)

    return out

def solveCase(case):
    # If the case is already solved... return case
    if(checkSolution(case) == 1):
        return case
    # Else, solve the case :3
    else:
        out = calcSolution(case)
        return out
# ---------------------------------------------------------------------------- #

# MAIN #
# ---------------------------------------------------------------------------- #
cases = input()
cases = int(cases)
if(DEBUG): print(cases)

if(cases >= 1 and cases <= 100):
    for i in range(0, cases):
        curCase = input()
        curCase = int(curCase)
        if(DEBUG): print("Case #" + str(i + 1) + ": " + str(curCase))

        res = solveCase(curCase)
        print("Case #" + str(i + 1) + ": " + str(res))
# ---------------------------------------------------------------------------- #
