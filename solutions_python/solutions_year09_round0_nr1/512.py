import sys
import re

letters, words, test_cases = map(lambda i: int(i), sys.stdin.readline().strip().split(" "))

known_words = []
for word in range(words):
    known_words.append(sys.stdin.readline().strip())

for case in range(test_cases):
    unknown = sys.stdin.readline().strip()
        
    number_of_matches = 0
    
    if "(" in unknown or ")" in unknown:
        pattern = ""
        
        in_paren = True
        skip_next = True
        for c in unknown:               
            if in_paren and not skip_next:
                pattern += "|" + c
            else:
                pattern += c
                
            skip_next = False
            if c == "(":
                in_paren = True
                skip_next = True
                continue
            elif c == ")":
                pattern = pattern[0:len(pattern)-2]
                pattern += ")"
                in_paren = False
                continue
            
        for known_word in known_words:
            if re.match(pattern, known_word):
                number_of_matches += 1

    else:
        if unknown in known_words:
            number_of_matches += 1

    print "Case #" + str(case + 1) + ": " + str(number_of_matches)