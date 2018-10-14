"""
Tidy Numbers
"""

OUTPUT = 'Case #%d: %ld'

def is_tidy(number):
    """
    count leading digits in correct order
    """
    numstr = str(number)
    #works only on +ve numbers and much faster
    #than backward way
    for i in range(len(numstr)-1):
        if numstr[i] > numstr[i+1]:
            return (False, len(numstr) - (i + 1))
    return (True, 0)


def main():
    T = int(raw_input().strip())

    for test in range(1, T + 1):
        N = int(raw_input().strip())

        while True:
            _verify = is_tidy(N)
            if _verify[0] is True:
                print OUTPUT % (test, N)
                break
            else:
                #number of digits to discard _verify[1]
                factor = 10 ** _verify[1]
                N = ((N / factor) * factor) - 1

if __name__ == '__main__':
    main()
