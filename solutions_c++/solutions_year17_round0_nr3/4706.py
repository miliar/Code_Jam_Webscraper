#include<bits/stdc++.h>
using namespace std;

int n, k, a, b, t;
multiset<int> con;


int main(){
	scanf("%d", &t);
	for(int c=1; c<=t; c++){
		scanf("%d %d", &n, &k);
		con.clear();
		con.insert(n);			
		
		for(int i=1; i<=k; i++){
			set<int>:: iterator it=con.end();
			it--;
			int m=*it;
				
			con.erase(it);
			a=m/2;
			if(m%2==0) b=m/2-1;	
			if(m%2==1) b=m/2;
			con.insert(a);
			con.insert(b);
			if(i==k){
				printf("Case #%d: %d %d\n", c, a, b);
			}
		}
		
	}
	
	return 0;	
}
