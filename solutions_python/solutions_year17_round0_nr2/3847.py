def tidy(number):
    return list(number) == sorted(list(number))

def solve(limit):
    for number in range(limit, 0, -1):
        if tidy(str(number)):
            return number 
    return 1

if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        k = int(input())
        print("Case #" + str(test + 1) + ": " + str(solve(k)))

