map_dict = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
with open('A-small-attempt1.out', 'w') as fout:
	with open('A-small-attempt1.in', 'r') as fin:
		cnt=0
		for line in fin:
			if not cnt:
				cnt+=1
				continue
			line=line.strip()		
			str_list=[]
			for chr in line:
				if chr == ' ':
					str_list.append(' ')
					continue
				str_list.append(map_dict[chr])
			fout.write("Case #" + str(cnt) + ": " + ''.join(str_list) + '\n')
			cnt+=1