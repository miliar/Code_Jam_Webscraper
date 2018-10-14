import string

def main():
    num_letters, num_words, num_deciphers = map(int, (raw_input().split()))
    all_words = []
    for i in range(num_words):
        all_words.append(raw_input())
    for case in range(num_deciphers):
        decipher = raw_input()
        possible_letters = ['' for i in range(num_letters)]
        letter_index = 0
        decipher_index = 0
        while decipher_index < len(decipher) and letter_index < num_letters:
            if decipher[decipher_index] == '(':
                next_index = string.find(decipher, ')', decipher_index)
                if next_index >= 0:
                    possible_letters[letter_index] = decipher[decipher_index + 1:next_index]
                    letter_index += 1
                    decipher_index = next_index + 1
                else:
                    decipher_index += 1
            elif decipher[decipher_index] == ')':
                decipher_index += 1
            else:
                possible_letters[letter_index] = decipher[decipher_index]
                letter_index += 1
                decipher_index += 1
        num_matches = 0
        for word in all_words:
            if all(map(lambda x, y: x in y, word, possible_letters)):
                num_matches += 1
        print "Case #%d: %d" % (case + 1, num_matches)
        
main()
