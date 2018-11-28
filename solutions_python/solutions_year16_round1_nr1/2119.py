
small_data_set = 200
large_data_set = 1000


def main():
    test_case = input()

    t = int(test_case)
    if not 1 <= t or not t <= 100:
        print('1 <= T <= 100')
        return

    index = 1
    for i in range(t):
        input_word = input()

        result_list = []
        word_list = list(input_word)

        if len(word_list) == 1:
            print('Case #{}: {}'.format(index, input_word))
            index += 1
            continue

        first_word = word_list.pop(0)
        second_word = word_list.pop(0)

        word = first_word + second_word
        word1 = second_word + first_word

        result_list.append(word)
        result_list.append(word1)

        while len(word_list) != 0:
            first_word = word_list.pop(0)

            temp_list = []
            for obj in result_list:
                temp_list.append(first_word + obj)
                temp_list.append(obj + first_word)

            result_list = temp_list

        result_list.sort()
        print('Case #{}: {}'.format(index, result_list[len(result_list)-1]))
        index += 1

main()




