tests = int(raw_input())

for i in range(tests):
    result = 0
    s_max , audience_number = map(str, raw_input().split())
    s_max = int(s_max)
    #print "smax: " + str(s_max)
    audience_string = str(audience_number)
    total_standing = 0
    
    for j in range(s_max+1):
	if total_standing < j:
		diff = j - total_standing
		result = result + diff
		total_standing = total_standing + diff
	total_standing = total_standing + int(audience_string[j])

    print 'Case #'+ str(i+1)+': '+ str(result)
