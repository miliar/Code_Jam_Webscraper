#include <bits/stdc++.h>
#define ll long long
using namespace std;

int f;
ll fn(ll n, ll k){
	if(k==1){
		if(n%2==1)
		    f=1;
		else 
		    f=2;
			return n/2;
	}
	if(k==2){
			return fn(n/2,k-1);
	}
	if(k>2){
		if(n%2==1){
			if((k-1)%2==0){
				return fn(n/2,(k-1)/2);
			}
			else
				return fn(n/2,(k-1)/2+1);
		}
		else{
			if((k-1)%2==0)
				return fn(n/2-1,(k-1)/2);
			else
				return fn(n/2,(k-1)/2+1);
		}
	}
}

int main(){
	int t,c=0;
	cin>>t;
	ll n,k;
	ll ans;
	while(t--){
	    c++;
		cin>>n>>k;	
		ans = fn(n,k);
		if(f==1)
		cout<<"Case #"<<c<<": "<<ans<<" "<<ans<<endl;
		else
		cout<<"Case #"<<c<<": "<<ans<<" "<<ans-1<<endl;
	}
	return 0;
}