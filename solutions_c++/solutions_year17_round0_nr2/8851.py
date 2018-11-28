#include<bits/stdc++.h>
#define ll long long int
using namespace std;
ll getLastTidy(ll n){
	ll ans;
	for(ll i=1;i<=n;i++){
        string p=to_string(i);
        if(is_sorted(p.begin(),p.end())){
            ans=i;
        } 
    }
	return ans;	
}

int main()
{  
    ll T,N;
    scanf("%lld",&T);
    for(ll t=1;t<=T;t++){
    	scanf("%lld",&N);
        ll res=getLastTidy(N); 
    	printf("Case #%lld: %lld\n",t,res);
	}
   return 0;   
}

