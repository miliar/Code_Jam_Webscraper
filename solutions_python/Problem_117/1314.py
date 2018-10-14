#!/usr/bin/env python
import sys
case_count = 1
def cprint(msg):
    global case_count
    print("Case #" + str(case_count) + ": " + msg)
    case_count += 1

def strToLawn(lawnStr):
    ret = []
    for line in lawnStr.split('\n'):
        try:
            line = [int(x) for x in line.strip().split(' ')]
        except ValueError:
            pass
        else:
            ret.append(line)
    return ret
        #if line != []:
        #    ret.append(line)

def canMow(lawn):
    for coordX in range(len(lawn[0])):
        for coordY in range(len(lawn)):
            targetHeight = lawn[coordY][coordX]
            def canHorizontally():
                for innerCoordX in range(len(lawn[0])):
                    if lawn[coordY][innerCoordX] > targetHeight:
                        return False
                return True
            def canVertically():
                for innerCoordY in range(len(lawn)):
                    if lawn[innerCoordY][coordX] > targetHeight:
                        return False
                return True
            if not (canHorizontally() or canVertically()):
                return False
    return True


def act(lawnStr):
    lawn = strToLawn(lawnStr)
    if canMow(lawn):
        cprint("YES")
    else:
        cprint("NO")

def main():
    current = ""
    current_height = None
    state = "skipfirst"
    for line in open(sys.argv[1]):
        if state == "skipfirst":
            state = "size"
        elif state == "size":
            state = "lawn"
            try:
                current_height = int(line.split(' ')[0])
            except ValueError:
                sys.exit(0)
        elif state == "lawn":
            current += line
            current_height -= 1
            if current_height == 0:
                state = "size"
                act(current)
                current = ""

if __name__ == '__main__':
    main()
