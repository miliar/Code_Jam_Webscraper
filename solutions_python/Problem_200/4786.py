def ProblemB():
    test_cases = int(input())
    numbers = [int(input()) for _ in range(test_cases)]
    case_number = 1
    for number in numbers:
        for i in reversed(range(1, number+1)):
            # check if tidy
            previous_number = 0
            for s in str(i):
                if int(s) >= previous_number:
                    previous_number = int(s)
                else:
                    break
            else:
                print("Case #", case_number, ": ", i, sep="")
                case_number += 1
                break

if __name__ == "__main__":
    ProblemB()