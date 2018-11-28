def solve(shyness):
    friend_count = 0
    stand_count = 0
    level = 0
    for shy_total in shyness:
        if stand_count < level:
            extra = level - stand_count
            friend_count += extra
            stand_count += extra

        stand_count += shy_total

        level += 1

    return friend_count


if __name__ == "__main__":
    f = open('jam_6224486.in', 'r')
    fout = open('jam_6224486.out', 'w')
    example_num = int(f.readline())

    for i in range(example_num):
        line = f.readline()
        max_shy, sequence = line.split(" ")
        max_shy = int(max_shy)

        shy_totals = []
        for j in range(max_shy + 1):
            shy_totals.append(int(sequence[j]))

        result_message = "Case #" + str(i + 1) + ": " + str(solve(shy_totals))
        print(result_message)
        fout.write(result_message + '\n')
