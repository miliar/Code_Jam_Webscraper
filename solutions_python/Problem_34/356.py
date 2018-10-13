def read_file(filename):
    fp = open(filename)
    lines = fp.readlines()
    return lines

def alien_language(filename):
    final_string = ""
    lines = read_file(filename)
    nums = lines[0]
    nums = nums.split()
    l = int(nums[0])
    d = int(nums[1])
    n = int(nums[2])
    words = []
    for x in range(d):
        words.append(lines[x+1][:l])
    for x in range(n):
        test_case = lines[d+x+1]
        letters = split_into_letters(test_case,l)
        num_words = 0
        for w in words:
            if word_match(w,letters):
                num_words = num_words + 1
        final_string = final_string + "Case #" + str(x+1)+ ": " + str(num_words) + "\n"
    return final_string

            
def word_match(word, letters):
    for i in range(len(word)):
        if not word[i] in letters[i]:
            return False
    return True

def split_into_letters(string,l):
    letters = []
    index = 0
    for x in range(l):
        this_letter = ""
        char = string[index]
        index = index + 1
        if char == "(":
            char = string[index]
            while char != ")":
                this_letter = this_letter + char
                index = index + 1
                char = string[index]
            if x < l - 1:
                index = index + 1
                char = string[index]
        else:
            this_letter = char
        letters.append(this_letter)
    return letters

def run(filename):
    a = open("output.txt","w")
    a.write(alien_language(filename))

run("A-large.txt")
