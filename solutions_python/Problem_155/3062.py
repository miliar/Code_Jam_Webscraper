file_object = open('A-large.in')  
try:  
     all_the_text = file_object.readlines( )
	
finally:  
     file_object.close( )
	 
output_text = open('output_text.in' , 'w')
for t in range(len(all_the_text) - 1):

    a = list(map(int, list(all_the_text[t + 1].split()[1])))

    s = ans = 0

    for i in range(len(a)):
        if i > s:
            ans += i - s
            s = i
        s += a[i]
	
    print('Case #%d: %s \r' % (t + 1, ans) , file=output_text)