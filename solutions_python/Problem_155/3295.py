__author__ = 'saurabh'


def main():

    input_file = open('/home/saurabh/Downloads/A-large.in', 'r')
    output_file = open('/home/saurabh/Downloads/jam1_out', 'w')

    cases = int(input_file.readline())

    for case_num in range(1, cases + 1):
        n, s = input_file.readline().split()
        n = int(n)

        people_standing = ord(s[0])-ord('0')
        people_needed = 0

        for i in range(1, n+1):
            if i > people_standing:
                people_needed += i - people_standing
                people_standing = i + ord(s[i]) - ord('0')
            else:
                people_standing += ord(s[i]) - ord('0')

        s = "Case #%d: %d\n" % (case_num, people_needed)

        output_file.writelines(s)

        cases -= 1

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()