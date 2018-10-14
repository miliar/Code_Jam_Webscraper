import fileinput

testcase_count = int(input())
for testcase_index in range(testcase_count):
    row1_index = int(input())
    for row in range(1, 5):
        cards = input()
        if row == row1_index:
            selected_row1 = cards.split()
    row2_index = int(input())
    for row in range(1, 5):
        cards = input()
        if row == row2_index:
            selected_row2 = cards.split()
    common_cards = set(selected_row1).intersection(set(selected_row2))
    if len(common_cards) == 0:
        result = "Volunteer cheated!"
    elif len(common_cards) > 1:
        result = "Bad magician!"
    else:
        result = str(common_cards.pop())
    print("Case #%d: %s" % (testcase_index + 1, result))
