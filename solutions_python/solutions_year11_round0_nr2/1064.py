def main():
	n=raw_input()
	k=0
	
	for k in range(int(n)):	
		t=raw_input().split( )
		c=t[0]
		
		if c=='1':
			comb=t[1]
			d=t[2]
			if d=='1':
				opp=t[3]
				st=t[5]
			else:
				st=t[4]
	
		else:
			d=t[1]
			if d=='1':
				opp=t[2]
				st=t[4]
			else:
				st=t[3]
		
	
		ans=['0']
		i=0
		for i in range(len(st)):
			ans.append(st[i])
#			print(ans)
			if c=='1':
				if st[i]==comb[0]:
					if ans[len(ans)-2]==comb[1]:
						ans.pop()
						ans.pop()
						ans.append(comb[2])
						continue
						
				else:
					if st[i]==comb[1]:
						if ans[len(ans)-2]==comb[0]:
							ans.pop()
							ans.pop()
							ans.append(comb[2])
							continue
			if d=='1':
				if st[i] == opp[0]:
					if opp[1] in ans:
						ans=['0']
						continue
		
				elif st[i] == opp[1]:
					if opp[0] in ans:
						ans=['0']
						continue
	
			
	
		ans.pop(0)
		j=0
		
		if len(ans)>1:
			s=''
			while j<len(ans)-1:
				s=s+ans[j]+', '
				j=j+1
			print('Case #'+str(k+1) +': ['+s+ans[j]+']')
		else:
			if len(ans)==1:
				print('Case #'+str(k+1)+ ': ['+ans[0]+']')
			if len(ans)==0:
				print('Case #'+str(k+1)+ ': []')
		
		
main()	
			
				 
		

	
