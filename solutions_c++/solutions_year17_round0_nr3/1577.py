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
multiset<ll> s;
multiset<ll>::iterator it;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>n>>k;
		s.insert(n);
		ll ans,x,y;
		while(k--){
			it = s.end();
			it--;
			ans = *it;
			s.erase(it);
			x = ans/2;
			y = ans-1-x;
			if(x > 0)
				s.insert(x);
			if(y > 0)
				s.insert(y);
		}
		cout<<"Case #"<<t<<": "<<x<<" "<<y<<"\n";
	}
	
	return 0;
}

