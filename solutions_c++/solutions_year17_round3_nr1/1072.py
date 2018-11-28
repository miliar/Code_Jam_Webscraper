#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define pb push_back
#define ff first
#define ss second
using namespace std;

ll n,k,tc;
pp cake[1010];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		multiset<ll> ms;
		multiset<ll>::iterator it;
		cin>>n>>k;
		for(ll i=0;i<n;i++){
			cin>>cake[i].ff>>cake[i].ss;
		}
		sort(cake,cake+n);
		ll sum = 0;
		ll ans = 0;
		for(ll i=0;i<k;i++){
			ms.insert(2*cake[i].ff*cake[i].ss);
			sum += 2*cake[i].ff*cake[i].ss;
		}
		ans = cake[k-1].ff*cake[k-1].ff + sum;
		for(ll i=k;i<n;i++){
			it = ms.begin();
			sum -= *it;
			ms.erase(it);
			ms.insert(2*cake[i].ff*cake[i].ss);
			sum += 2*cake[i].ff*cake[i].ss;
			ans = max(ans,sum+cake[i].ff*cake[i].ff);
		}
		double temp = ans*(4*atan(1));
		cout<<"Case #"<<t<<": "<<fixed<<temp<<"\n";
	}
	
	return 0;
}

