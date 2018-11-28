#include <bits/stdc++.h>
using namespace std;
typedef long long lli;


int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		lli n,k;
		scanf("%lld %lld",&n,&k);
		lli s=n+2;
		while(k>1){
			if(k%2 == 0) s=s/2+1;
			else s=(s+1)/2;
			k/=2;
		}
		s=s-3;
		printf("Case #%d: %lld %lld\n",t,(s+1)/2,s/2);
	}
}