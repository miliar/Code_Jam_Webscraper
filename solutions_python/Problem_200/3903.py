def TidyNumbers(N):
    output = str(N)
    for i in range(len(output) - 2, -1, -1):
        if output[i] > output[i + 1]:
            newchar = str(int(output[i]) - 1)
            output = output[:i] + newchar + "9"*(len(output) - i - 1)

    output = output[1:] if output.startswith("0") else output
    return output

t = int(input())
for i in range(1, t + 1):
    N = int(input())
    output = TidyNumbers(N)
    print("Case #{}: {}".format(i, output))
