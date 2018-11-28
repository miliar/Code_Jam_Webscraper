#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll r[1000];
vector<ll> arr[1000];
int main(){
	ll t;
	cin>>t;
	for(ll z=1;z<=t;++z){
		ll n,p;
		cin>>n>>p;
		for(ll i=0;i<n;++i)
			cin>>r[i];
		for(ll i=0;i<n;++i){
			vector<ll> vec;
			for(ll j=0;j<p;++j){
				ll x;
				cin>>x;
				vec.push_back(x);
			}
			sort(vec.begin(),vec.end());
			reverse(vec.begin(),vec.end());
			arr[i]=vec;
		}
		ll ans=0,mult=1;
		while(true){
			bool cut=false;
			ll ok=0;
			for(ll i=0;i<n;++i){
				while(arr[i].size()){
					if(mult*r[i]*9>arr[i].back()*10) arr[i].pop_back();
					else break;
				}
				if(arr[i].size()==0){
					cut=true;
					break;
				}
				ll val=arr[i].back();
				if(mult*r[i]*9<=val*10&&val*10<=mult*r[i]*11)
					++ok;
			}
			if(cut) break;
			if(ok==n){
				++ans;
				for(ll i=0;i<n;++i)
					arr[i].pop_back();
			}
			for(ll i=0;i<n;++i){
				if(arr[i].size()==0){
					cut=true;
					break;
				}
				ll den=r[i]*11;
				mult=max(mult,(arr[i].back()*10+den-1)/den);
			}
			if(cut) break;
		}
		printf("Case #%lld: %lld\n",z,ans);
	}
}