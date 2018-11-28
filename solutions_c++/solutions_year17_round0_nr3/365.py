#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	long long sc,lc,n,k;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%lld%lld",&n,&k);
		sc=1;
		lc=0;
		while(k>sc+lc){
			k-=sc+lc;
			if(n&1){
				sc=sc*2+lc;
			}
			else{
				lc=lc*2+sc;
			}
			n=(n-1)/2;
		}
		if(k<=lc) n++;
		printf("Case #%d: %lld %lld\n",cs,n/2,(n-1)/2);
	}
	return 0;
}
