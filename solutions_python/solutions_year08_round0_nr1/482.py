text_file = open("A-large.in.txt","r")
number_of_trials = int(text_file.readline())
for i in range(1,number_of_trials + 1,1):
    num_search = -1
    num_q = -1
    n = 0
    num_search = int(text_file.readline())
    qs = []
    searches = {}
    for j in range(1,num_search + 1,1):
        searches[text_file.readline()] = 0
    num_q = int(text_file.readline())
    for j in range(1,num_q + 1,1):
        qs_new = [text_file.readline()]
        qs += qs_new
    for curr_q in qs:
        if searches[curr_q] == n:
            searches[curr_q] = n + 1
        if n in searches.values():
            n = n
        else:
            n = n + 1
            searches[curr_q] = n + 1
    print "Case #"+str(i)+": "+str(n)
