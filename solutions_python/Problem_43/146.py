import string

def read(filename):
    result = []
    input = open(filename, 'r')
    cases = int(input.readline())
    for i in xrange(cases):
        result.append(input.readline().strip())
    input.close()
    return result

def to_number(message):
    letters = {}
    result = ""
    indexes = '1023456789' + string.lowercase
    index = 0
    for letter in message:
        position = letters.get(letter)
        if position is None:
            letters[letter] = indexes[index]
            position = indexes[index]
            index += 1
        result += position
    return int(result, max(2, len(letters)))

if __name__ == "__main__":
    for index, line in enumerate(read("A-large.in")):
        print "Case #%d: %d" % (index + 1, to_number(line))
