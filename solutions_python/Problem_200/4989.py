def find_tidy(n):
    for num in range(n+1):
        for i, number in enumerate(str(num)):
            try:
                if int(str(num)[i+1]) < int(number):
                    break
            except IndexError:
                tidy = num
    return tidy


if __name__ == "__main__":
    with open("B-small-attempt0.in") as f:
        answers = []
        lines = f.readlines()

        iterations = lines[0]
        nums = lines[1:]
        output = []
        for line in nums:
            answers.append(find_tidy(int(line)))
        for i, answer in enumerate(answers):
            output.append("Case #{0}: {1}\n".format(i+1, answer))

        with open("small_output.txt", "w") as f2:
            for line in output:
                f2.write(line)
