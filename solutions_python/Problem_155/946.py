#-*- coding: utf-8 *-*
t = int(raw_input(""))
for i in range(1,t+1):
	s = raw_input("")
	s = s.split(" ")[1]
	needed_friends = 0
	already_standing = 0
	for cur_shynes, num_of_persons in enumerate(s):
		needed_friends += max(0, (cur_shynes - already_standing - needed_friends))
		already_standing += int(num_of_persons)
	print "Case #%s: %s" % (i, needed_friends)


