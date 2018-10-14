import sys

def main(input_path):
    opposite_status = { '-':'+', '+':'-'}

    input_file = open(input_path, 'rb')
    tests_amount = int(input_file.readline())
    tests = input_file.readlines()

    for j in range(tests_amount):
        panckaes, flipper_size = tests[j].split()
        pancakes_list = list(panckaes)
        flipper_size_num = int(flipper_size)
        counter = 0
        is_impossible = False

        for i in range(len(pancakes_list)):
	    	if pancakes_list[i] == '-':
	    	    if (i + flipper_size_num - 1) < len(pancakes_list):
	    		    for i in range(i, i + flipper_size_num):
	    		        pancakes_list[i] = opposite_status[pancakes_list[i]]
	    		    i += flipper_size_num
	    		    counter+=1
	    	    else:
	    			is_impossible = True
	    			break

        if is_impossible:
            print 'Case #{}: IMPOSSIBLE'.format(j + 1)
        else:
            print 'Case #{}: {}'.format(j + 1, counter)
        #print pancakes_list, counter






if __name__ == "__main__":
	main(sys.argv[1])