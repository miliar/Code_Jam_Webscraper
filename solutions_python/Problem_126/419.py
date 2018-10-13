__author__ = 'Christian Hersevoort'

import math

vowel = set("aeiou")

def is_special_string(string, n):
    global vowel
    counter = 0
    for letter in string:
        if letter in vowel:
            counter = 0
        else:
            counter += 1

        if(counter >= n):
            return True

    return False

def main():

    wp = open('test-file.out', 'w+')
    with open('A-small-attempt0.in') as fp:
        number_of_cases = int(fp.readline())
        for zz in range(0, number_of_cases):
            answer = 0
            (word, n) = fp.readline().strip('\n').split(' ')
            n = int(n)

            for start in range(0, len(word)):
                for end in range(0, len(word)):
                    wordz = word[start:end+1]
                    if is_special_string(wordz, n):
                        answer += 1







            """
            (low, high) = [int(n) for n in fp.readline().strip('\n').split(' ')]

            print low, high
            count = 0

            for x in range(0, 32):
                y = x * x

                if (y >= low) and (y <= high):
                    if is_palindrome(y) and is_palindrome(int(math.sqrt(y))):
                        count += 1
            """

            result = "Case #%d: %s\n" % (zz + 1, answer)
            wp.write(result)
            print result
if __name__ == "__main__":
    main()
