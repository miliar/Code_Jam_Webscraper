def solve_a():
    in_file = open("A-small.in")
    out_file = open("A.out", "w+")

    vowels = ['a', 'e', 'i', 'o', 'u']
    def is_vowel(c):
        try:
            return vowels.index(c) != -1
        except:
            return False

    assert is_vowel('a')
    assert not is_vowel('j')
    assert is_vowel('i')

    num_cases = int(in_file.readline())
    for case_index in range(num_cases):
        (name, ns) = tuple(
            [i for i in in_file.readline().split()]
        )

        n = int(ns)

        result_number = 0

        print(name)
        for i in xrange(len(name)):
            if not is_vowel(name[i]):
                j = i
                for j in xrange(i, len(name)):
                    if is_vowel(name[j]):
                        break
                print(i,j)

            if j - i - 1 >= n:
                result_number 

            i = j

        result = str(result_number)
        print(
            "Case " + str(case_index + 1) + ": " + str(result)
        )
        out_file.write(
            "Case " + str(case_index + 1) + ": " + str(result) + "\n"
        )
        out_file.flush()

    in_file.close()
    out_file.close()

def solve_b():
    in_file = open("B-small-attempt2.in")
    out_file = open("B.out", "w+")

    num_cases = int(in_file.readline())
    for case_index in range(num_cases):
        (x, y) = tuple(
            [int(i) for i in in_file.readline().split()]
        )

        result = ""

        if x > 0:
            if x == 1:
                result += "E"
            else:
                result += "E" + "WE" * (x - 1)
        if x < 0:
            if x == -1:
                result += "W"
            else:
                result += "W" + "EW" * (-x - 1)

        if y > 0 or y < 0:
            if y > 0:
                result += ("SN" * y)
            else:
                result += ("NS" * (-y))

        print(
            "Case #" + str(case_index + 1) + ": " + str(result)
        )
        out_file.write(
            "Case #" + str(case_index + 1) + ": " + str(result) + "\n"
        )
        out_file.flush()

    in_file.close()
    out_file.close()

def main():
    solve_b()

if __name__ == "__main__":
    main()