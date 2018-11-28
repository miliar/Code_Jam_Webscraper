def main():
    token = 'welcome to code jam'
    for case in range(input()):
        text = raw_input()
        prefix_combination = [[0 for i in range(len(token))] for j in range(len(text))]
        for text_index in range(len(text)):
            for token_index in range(len(token)):
                if text[text_index] == token[token_index]:
                    if token_index == 0:
                        prefix_combination[text_index][token_index] = 1
                    else:
                        combination = 0
                        for prefix_index in range(text_index):
                            combination += prefix_combination[prefix_index][token_index - 1]
                        prefix_combination[text_index][token_index] = combination
            
        total_combination = 0
        for text_index in range(len(text)):
            total_combination += prefix_combination[text_index][-1]
        total_combination_string = "%04d" % (total_combination)
        print "Case #%d: %s" % (case + 1, total_combination_string[:4])
        
main()
