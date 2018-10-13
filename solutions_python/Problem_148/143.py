with open('A.in') as f:
    with open('A.out', 'w') as f2:
        lines = f.readlines()
        output = ""

        for i in range(int(lines[0])):
            line1 = lines[i*2+1].split(" ")
            N = int(line1[0])
            X = int(line1[1])

            S = sorted([int(x) for x in lines[i*2+2].split(" ")])

            left_index = 0
            number_of_discs = 0
            right_index = len(S)-1
            while left_index <= right_index:
                if S[left_index] + S[right_index] <= X:
                    left_index += 1
                    right_index -= 1
                else:
                    right_index -= 1
                number_of_discs += 1
            output += "Case #" + str(i+1) + ": " + str(number_of_discs) + "\n"

        print(output)
        f2.write(output)