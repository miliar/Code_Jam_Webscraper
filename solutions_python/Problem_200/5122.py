""" Previous sorted number """

def prev_sorted_number() -> None:
    """ Main module to get the previous sorted number """
    filename = "B-small-attempt0"
    try:
        with open(filename + ".in", "r") as inputfile:
            with open(filename + ".out", "w") as outputfile:
                shouldcontinue = True
                caseindex = 1
                for line in inputfile:
                    if shouldcontinue:
                        shouldcontinue = False
                        continue
                    print("Case #{0}: ".format(caseindex), end="", file=outputfile)
                    strnumber = line.rstrip("\n")
                    # check if the given number is in its sorted format
                    if "".join(sorted(strnumber)) == strnumber:
                        print(strnumber, file=outputfile)
                    else:
                        number = int(strnumber)
                        while True:
                            number -= 1
                            digitlist = [int(digit) for digit in str(number)]
                            if sorted(digitlist) == digitlist:
                                print("{0}".format(number), file=outputfile)
                                break
                    caseindex += 1
    except ValueError as valerr:
        print(valerr.args)
    except NameError as nameerr:
        print(nameerr.args)
    except TypeError as typeerr:
        print(typeerr.args)
    except IOError as ioerr:
        print(ioerr.args)
    except KeyboardInterrupt:
        print("Operation Interrupted!!")

if __name__ == "__main__":
    prev_sorted_number()
