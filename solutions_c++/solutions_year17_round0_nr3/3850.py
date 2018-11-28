#include <bits/stdc++.h>

using namespace std;

typedef long long ll;



ll pw(ll x){
	if(x==0)return 1;
	ll v = pw(x/2);
	if(x%2)return v*(v<<1);
	else return v*v;

}

int main(){
	ll tc=1,t;
	scanf("%lld",&t);
	while(tc<=t){
		ll n,k,x;
		scanf("%lld%lld",&n,&k);
		x = ceil(log(k+1)/log(2));

		x = pw(x-1);

		ll lw = x-1;
		ll l = 0,r = n;

		while(l<r){
			ll mid = (l+r+1)/2;
			if((mid*x)<=n-lw){
				l = mid;
			}else{
				r = mid - 1;
			}
		}

		ll ls,rs,y = n-lw-(l*x);

		if(k-lw<=y){
			ls = l/2;
			rs = (l+1)/2;
		}else{
			ls = (l-1)/2;
			rs = l/2;
		}


		ls = max(ls,0LL);
		rs = max(rs,0LL);
		printf("Case #%lld: %lld %lld\n",tc,max(ls,rs),min(ls,rs) );
		tc++;
	}
	return 0;
}