#include "bits/stdc++.h"
#define ll long long
#define K ll t; cin>>t; for(ll Th=1;Th<=t;Th++)
using namespace std;
ll temp[30];

bool istidy(ll sz){
	for(int i=1;i<sz;i++){
		if(temp[i]<temp[i-1]) return false;
	}
	return true;
}

ll count(ll p){
	ll ct=0;
	while(p>=1){
		p/=10;
		ct++;
	}
	return ct;
}

int main(){
	K{
		ll a[30],res=0;;
		ll n; cin>>n; ll x=n;
		ll sz=count(n);
		//cout<<sz;
		for(ll z=sz-1;z>=0;z--) a[z]=n%10,n/=10;
		for(ll i=0;i<sz;i++) temp[i]=a[i];
		
		if(istidy(sz)){
			//cout<<"HELLO";
			cout<<"Case #"<<Th<<": "<<x<<'\n';	
				continue;
		}
		ll z=sz-2;
		while(1){
			
			for(ll i=0;i<sz;i++) temp[i]=a[i];
			
			temp[z]=temp[z]-1;
			for(ll i=z+1;i<sz;i++) temp[i]=9;
			//for(ll i=0;i<sz;i++) cout<<temp[i]<<" "; cout<<'\n';
			if(istidy(sz)){
				cout<<"Case #"<<Th<<": ";
				if(z==0 && temp[z]==0) {for(ll i=1;i<sz;i++) cout<<temp[i]; cout<<'\n';break;}
				else {for(ll i=0;i<sz;i++) cout<<temp[i];cout<<'\n'; break;}
				
			}
			z--;
		}
			//cout<<"Case #"<<Th<<": "<<res<<'\n';
	}
	
	return 0;
}
