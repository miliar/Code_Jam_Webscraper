if __name__ == "__main__":
    with open("input.txt", "r") as input:
        with open("output.txt", "w+") as output:
            T = int(input.readline())
            for t in range(T):
                line = input.readline()
                tokens = line.split(" ")
                S_max = int(tokens[0])
                shyness_string = tokens[1]
                shyness_counts = [None] * (S_max + 1)
                for s in range(S_max + 1):
                    shyness_counts[s] = int(shyness_string[s])
                additional_audience = 0
                cumulative_audience = shyness_counts[0]
                for s in range(1, S_max + 1):
                    if cumulative_audience < s:
                        additional_audience += (s - cumulative_audience)
                        cumulative_audience = s
                    cumulative_audience += shyness_counts[s]
                print("Case #{0}: {1}".format(t + 1, additional_audience), file=output)