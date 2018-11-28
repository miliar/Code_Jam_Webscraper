/*
 *	Task: C. Bathroom Stalls
 *	Lang: C/C++11
 *	Author: comtalyst
 *	Site: Google Code Jam 2017 Qualification Round
 *	Last Update: 8/4/2017
 */

#include <bits/stdc++.h>
//#pragma GCC optimize ("O3")
using namespace std;

/* Note
Large input supported
Learned :  
*/	

#define x first
#define y second
#define umap unordered_map
#define pqueue priority_queue
#define mset multiset
#define mp make_pair

long long a[136],b[136],c[136];

main(){
	long long t,i,j,n,m,tt=0,v,y=1,x,bx;	
	freopen("C-l-in.txt","r",stdin);
	freopen("C-l-out.txt","w",stdout); 
	
	scanf("%lld",&t);
	while(t--){
		memset(a,0,sizeof a);
		memset(b,0,sizeof b);
		memset(c,0,sizeof c);
		scanf("%lld %lld",&n,&x);
		i = 1;
		v = n;
		y = 1;
		if(n%2 == 0){
			b[1] = 1;
		}
		else{
			a[1] = 1;
		}
		bx = x;
		x--;
		y *= 2;
		while(x > 0){
			i++;
			v /= 2;		//v is last value (before this)
			bx = x;
			x -= y;
			y *= 2;
			if(v%2 == 0){
				b[i] = b[i-1] + a[i-1]*2;
				c[i] = b[i-1] + c[i-1]*2;
			}
			else{
				a[i] = b[i-1] + a[i-1]*2;
				b[i] = b[i-1] + c[i-1]*2;
			}
//			printf("%lld = %lld : %lld %lld %lld\n",i,v/2,a[i],b[i],c[i]);
		}
		x = bx;
		x -= a[i];
		v /= 2;
		if(x <= 0){
			printf("Case #%lld: %lld %lld\n",++tt,v,v); //a
		}
		else{
			x -= b[i];
			if(x <= 0){
				printf("Case #%lld: %lld %lld\n",++tt,v,v-1); //b	
			}
			else{
				printf("Case #%lld: %lld %lld\n",++tt,v-1,v-1); //c
			}
		}
	}
	
	return 0;	
}


















