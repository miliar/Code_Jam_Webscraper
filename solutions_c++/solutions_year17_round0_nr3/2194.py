#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	ll pows[61];
	pows[0]=1;
	for(int i=1;i<=60;i++)
		pows[i]=pows[i-1]*2;
	int t;
	cin >> t;
	ll n,k;
	for(int z=1;z<=t;z++){
		scanf("%lld%lld",&n,&k);
		ll k1=k;
		int j=0;
		while(true){
			if(k1-pows[j]<=0)
				break;
			k1-=pows[j++];
		}
		ll val1=(n-(pows[j]-1))/pows[j];
		ll cnt1=pows[j]-(n-(pows[j]-1))%pows[j];
		ll val2=(n-(pows[j]-1))/pows[j]+1;
		ll cnt2=(n-(pows[j]-1))%pows[j];	
		/*pows[j]-(n-(pows[j]-1))%pows[j]  times  -> (n-(pows[j]-1))/pows[j]
		(n-(pows[j]-1))%pows[j] times -> (n-(pows[j]-1))/pows[j]+1  -> */
		if(k1<=cnt2){
			ll minval=(val2%2==1)?val2/2:val2/2-1;
			ll maxval=val2/2;
			printf("Case #%d: %lld %lld\n",z,maxval,minval);
		}
		else{
			ll minval=(val1%2==1)?val1/2:val1/2-1;
			ll maxval=val1/2;
			printf("Case #%d: %lld %lld\n",z,maxval,minval);
		}
	}	
	return 0;
}