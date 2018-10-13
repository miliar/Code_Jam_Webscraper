# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:02:49 2017

@author: Billoier

1"""
maxn = 10000;

Q = list();
visit = set();

           
def Transform(now,index,k):
  #print(now+str(index)+' '+str(k)+'\n');
  now = list(now);
  
  for i in range(k):
      now[index+i] = str(int(now[index+i])^1);
  return ''.join(now)


def check(now):
	for key in now:
		if (key!='1'):
			return False;
	return True;


def BFS(have,k):
	head = 0;
	tail = 0;
	Q.clear();
	visit.clear();

	length = len(have);
	key = [have,0];  
	Q.append(key);
	visit.add(have);
	while(head<=tail):
		current = Q[head];
		for i in range(length-k+1):
			then = Transform(current[0],i,k);
			if(check(then)):
				return current[1]+1;
			if(not(then in visit)):
				visit.add(then)
				key = [then,current[1]+1];
				tail = tail + 1;
				#if(tail>len(Q)):
				Q.append(key);
		head = head + 1;
	return False;


if __name__=='__main__':
    
    Test_Num = int(input().strip());
    
    for i in range(Test_Num):
    	line = input().strip();
    	have = line.split(' ')[0].strip().replace('+','1');
    	have =  have.replace('-','0'); 
    	k = int(line.split(' ')[1].strip());
    	if(check(have)):
    		print('Case #'+str(i+1)+': 0');
    	else:
    		ans = BFS(have,k);
    		if(ans):
    			print('Case #'+str(i+1)+': '+str(ans));
    		else:
    			print('Case #'+str(i+1)+': '+'IMPOSSIBLE');
            
        