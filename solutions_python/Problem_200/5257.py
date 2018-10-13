def tidy_numbers(t, n):

	n_list = [int(i) for i in list(str(n))]

	if len(n_list) > 1:

		while [int(i) for i in n_list] != sorted([int(i) for i in n_list]):

			n -= 1
			n_list = [int(i) for i in list(str(n))] 


	print ("Case #%i: %s" % (t, ''.join([str(i) for i in n_list])))

t = int(input())
for i in range(1, t + 1):

	tidy_numbers(i, int(input()))