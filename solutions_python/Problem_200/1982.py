T = int(raw_input())
test_cases = []
for case in xrange(T):
    test_cases.append(int(raw_input()))

for case in xrange(len(test_cases)):
    N_str = list(str(test_cases[case]))
    for i in xrange(len(N_str) - 2, -1, -1):
        if int(N_str[i]) > int(N_str[i+1]):
            N_str[i] = str(int(N_str[i]) - 1)
            N_str[i+1:] = "9" * len(N_str[i+1:])
    N_str = int("".join(N_str))
    answer = "Case #" + str(case + 1) + ": " + str(N_str) + "\n"
    print answer
