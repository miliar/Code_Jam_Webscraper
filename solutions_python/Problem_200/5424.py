def calculate(max):
    min_tidy = 1
    for i in range(1, max + 1):
        if is_tidy(i):
            min_tidy = i
    return min_tidy

def is_tidy(numbr):
    digits = str(numbr)
    initial = int(digits[0])
    for i in range(0, len(digits)):
        if int(digits[i]) < initial:
            return False
        else:
            initial = int(digits[i])
    return True

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T+1):
        input = int(f.readline().strip())
        solution = calculate(input)
        print("Case #{0}: {1}".format(case, solution))
