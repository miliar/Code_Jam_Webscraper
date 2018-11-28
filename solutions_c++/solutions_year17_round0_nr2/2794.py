#include<bits/stdc++.h>
using namespace::std;

int main(){
	int v[20];
	int t;
	long long n;
	scanf("%d",&t);
	for(int caso=1; caso<=t; caso++){
		printf("Case #%d: ",caso);
		scanf("%lld",&n);
		int pos = 0;
		while(n){
			v[pos++] = n%10;
			n/=10;
		}
		reverse(v,v+pos);
		bool is;
		int change;
		int carry = pos;
		while(carry){
			is = true;
			change = -1;
			for(int i=0; is && i<pos; i++){
				if(v[i]<v[i-1]){
					change = i-1;			
					is = false;
				}
			}
			carry--;
			if(change==-1){			
				continue;
			}
			v[change]--;
			for(int i=change+1; i<pos; i++) v[i] = 9;
		}
		int start = 0;
		while(v[start]<=0) start++;
		for(int i=start; i<pos; i++) cout << v[i];
		puts("");
		
	}
	return 0;
}
