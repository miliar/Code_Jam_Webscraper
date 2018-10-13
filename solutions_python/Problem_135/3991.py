def string_result(result):
	if len(result) == 1:
		return result.pop()
	elif len(result) == 0:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'

def main():
    txtin = open("input.txt", "r")
    cases = int(txtin.readline())
    writelines = []
    for case in range(1, cases+1):
        first_choice = int(txtin.readline())
        first_field = []
        for j in range(4):
            first_field.append(map(int,txtin.readline().split()))
        first_choice = set(first_field[first_choice-1])
        second_choice = int(txtin.readline())
        second_field = []
        for j in range(4):
            second_field.append(map(int,txtin.readline()[:-1].split()))
        second_choice = set(second_field[second_choice-1])
        result =  first_choice & second_choice
        res = "Case #%s: %s\n" % (case, string_result(result))
        writelines.append(res)
    txtout = open("output.txt", "w")
    txtout.writelines(writelines)
    txtout.close()

if __name__ == '__main__':
    main() 