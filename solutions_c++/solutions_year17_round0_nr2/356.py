#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		long long n,ans=0,a1=1;
		scanf("%lld",&n);
		long long r=1;
		while(r*10<=n) r*=10,a1+=r;
		while(r>=1){
			if(n/r*a1<=n){
				ans+=n/r*r;
			}
			else{
				ans+=(n/r)*r-1;
				break;
			}
			n%=r;
			a1/=10;
			r/=10;
		}
		printf("Case #%d: %lld\n",cs,ans);
	}
	return 0;
}