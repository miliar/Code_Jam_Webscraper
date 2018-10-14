def solve_a():
    in_file = open("A-small-attempt0.in")
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

    def nvalue(substr, n):
        i = 0
        while i < len(substr):
            if not is_vowel(substr[i]):
                j = i
                while j < len(substr):
                    if is_vowel(substr[j]):
                        break
                    j += 1

                if j - i >= n:
                    return True

                i = j
            else:
                i += 1
        return False

    assert nvalue("abcabcd", 3)
    assert nvalue("abc", 2)
    assert nvalue("abca", 2)

    num_cases = int(in_file.readline())
    for case_index in range(num_cases):
        (name, ns) = tuple(
            [i for i in in_file.readline().split()]
        )

        n = int(ns)

        result_number = 0

        for i in xrange(len(name)):
            for j in xrange(i + 1, len(name) + 1):
                if nvalue(name[i:j], n):
                    result_number += 1

        result = str(result_number)
        print(
            "Case #" + str(case_index + 1) + ": " + str(result)
        )
        out_file.write(
            "Case #" + str(case_index + 1) + ": " + str(result) + "\n"
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
    solve_a()

if __name__ == "__main__":
    main()