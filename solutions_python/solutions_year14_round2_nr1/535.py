testcase_count = int(input())
for testcase_index in range(testcase_count):
    n = int(input())
    words = []
    final_letter_order = ""
    possible = True
    for i in range(n):
        word = input()
        word_data = []
        letter_order = ""
        current_letter = ""
        current_count = 0
        letter_index = 0
        while True:
            if word[letter_index] == current_letter:
                current_count += 1
            else:
                if current_count > 0:
                    word_data.append(current_count)
                current_count = 1
                current_letter = word[letter_index]
                letter_order += current_letter
            
            letter_index += 1
            if letter_index == len(word):
                word_data.append(current_count)
                break
        if final_letter_order == "":
            final_letter_order = letter_order
        elif final_letter_order != letter_order:
            # Fegla won
            possible = False
            break
        words.append(word_data)

    if possible:
        moves = 0
##        print(words)
##        print(len(words[0]))
        for i in range(len(words[0])):
            total = 0
            for word in words:
                total += word[i]
            target = round(total / n)
            for word in words:
                moves += abs(target - word[i])
        
        result = str(moves)
    else:
        result = "Fegla Won"

    print("Case #%d: %s" % (testcase_index + 1, result))
