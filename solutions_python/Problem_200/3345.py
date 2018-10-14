def tidy_down(string):
    counter = 1
    rounded_down = False
    tidy2 = check_tidiness(string)
    while not tidy2:
        if not rounded_down:
            string = str(int(string) - (int(string) % 10) - 1)
            rounded_down = True
        else:
            string = str(int(string) - int(string[-counter:]) - 1)
        counter += 1
        tidy2 = check_tidiness(string)
    return string


def check_tidiness(string):
    i = 0
    while i < len(string) - 1:
        if string[i] > string[i + 1]:
            return False
        i += 1
    return True


results = []

with open("input/input.txt") as file:
    T = int(file.readline())  # Test cases
    counter = 1
    for line in file:
        if counter > T:
            break
        else:
            N = line.strip()
            tidy = check_tidiness(N)
            if tidy:
                # print("Case #%d: %s" % (counter, N))
                results.append("Case #%d: %s\n" % (counter, N))
            else:
                # print("Case #%d: %s" % (counter, tidy_down(N)))
                results.append("Case #%d: %s\n" % (counter, tidy_down(N)))
        counter += 1

with open("output/output.txt", 'w') as file:
    file.writelines(results)
