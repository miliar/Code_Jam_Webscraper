from collections import defaultdict

file_name = "A-large"


def read_file():
    with open(file_name+".in", "r") as f:
        f.readline()
        return list(map(str.strip, f.readlines()))


def write(lines):
    with open(file_name+".out", "w") as out:
        for index, answer in enumerate(lines):
            out.write("Case #"+str(index+1)+": "+str(answer)+"\n")


def count_word_occurrences(string):
    word_to_num = {
        "ZERO": 0,
        "ONE": 1,
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5,
        "SIX": 6,
        "SEVEN": 7,
        "EIGHT": 8,
        "NINE": 9,
    }
    frequency_order = [
        "ZERO",
        "SIX",
        "TWO",
        "FOUR",
        "FIVE",
        "SEVEN",
        "EIGHT",
        "NINE",
        "SIX",
        "THREE",
        "ONE"
    ]
    letter_frequency = defaultdict(lambda: 0)
    for letter in string:
        letter_frequency[letter] += 1
    words = []
    for number in frequency_order:
        while all(letter_frequency[char] for char in number):
            for char in number:
                letter_frequency[char] -= 1
            words.append(number)
    nums = [str(word_to_num[word]) for word in words]
    nums.sort()
    return "".join(nums)


write(map(count_word_occurrences, read_file()))
