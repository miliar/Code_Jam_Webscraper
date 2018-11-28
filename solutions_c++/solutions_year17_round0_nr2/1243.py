/*
 *	Task: B. Tidy Numbers
 *	Lang: C/C++11
 *	Author: comtalyst
 *	Site: Google Code Jam 2017 Qualification Round
 *	Last Update: 8/4/2017
 */

#include <bits/stdc++.h>
//#pragma GCC optimize ("O3")
using namespace std;

/* Note
Learned :  
*/	

#define x first
#define y second
#define umap unordered_map
#define pqueue priority_queue
#define mset multiset
#define mp make_pair

char str[23];

main(){
	int t,i,j,n,m,x,l,tt=0;	
	freopen("B-l-in.txt","r",stdin);
	freopen("B-l-out.txt","w",stdout);
	
	scanf("%d",&t);
	while(t--){
		scanf("%s",str+1);
		l = strlen(str+1);
		x = 1;
		while(x <= l && str[x] >= str[x-1]){
			x++;
		}
		if(x > l){
			printf("Case #%d: %s\n",++tt,str+1);
			continue;
		}
		for(i = x; i <= l; i++){
			str[i] = '9';
		}
		x--;
		while(str[x] == str[x-1]){
			str[x] = '9';
			x--;
		}
		str[x] = str[x]-1;
		if(str[x] < '0' || x < 1){
			str[l--] = '/0';
		}
		x = 1;
		while(x <= l && str[x] <= '0') x++;
		if(x > l){
			printf("Case #%d: 0\n",++tt);
		}
		else{
			printf("Case #%d: %s\n",++tt,str+x);
		}
	}
	
	return 0;	
}


















