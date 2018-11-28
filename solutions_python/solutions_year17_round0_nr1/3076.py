def flip(string):
    return string.replace("-", "=").replace("+", "-").replace("=", "+")


results = []

with open("input/input.txt") as file:
    T = int(file.readline())  # Test cases
    counter = 1
    for line in file:
        flips = 0
        if counter > T:
            break
        else:
            S, _, K = line.partition(" ")  # Pancake row
            K = int(K)  # Flip not fewer than K pancakes
            length = len(S)
            while 1:
                match_pos = S.find("-")
                if match_pos == -1:
                    print("Case #%d: %d" % (counter, flips))
                    results.append("Case #%d: %d\n" % (counter, flips))
                    break
                elif (match_pos + K) <= length:
                    S = S.replace(S[match_pos:match_pos + K], flip(S[match_pos:match_pos + K]), 1)
                    flips += 1
                else:
                    print("Case #%d: IMPOSSIBLE" % counter)
                    results.append("Case #%d: IMPOSSIBLE\n" % counter)
                    break
        counter += 1

with open("output/output.txt", 'w') as file:
    file.writelines(results)