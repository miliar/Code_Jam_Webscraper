"""
	Program:        2017 Code Jam Qualifications, Tidy Numbers
	Author:         Emily Sleeth
	Description:    Find the last tidy number counted
"""

"""
	Function:       is_tidy
	Purpose:        return true if a number is tidy
	Parameters:     a string of digits
"""
def is_tidy(num):
    for i in xrange(len(num)-1):
        j = i + 1
        if int(num[i]) > int(num[j]):
            return False

    return True

"""
	Function:       main
"""
def main():
    cases = int(raw_input())

    for n in range(cases):
        try:
            number = int(raw_input())
        except (EOFError):
            break

        tidy = is_tidy(str(number))
        while tidy == False:
            number -= 1
            tidy = is_tidy(str(number))

        out = "Case #" + str(n + 1) + ": " + str(number)
        print out

"""
    Runs the main
"""
if __name__ == "__main__":
    main()
