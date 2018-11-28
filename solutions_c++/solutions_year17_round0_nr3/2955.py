#include <bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef long double ld;
typedef vector<ll> vi;
typedef vector<pair<ll,ll> > vpii;
typedef pair<ll,ll> pii;

#define fr(i ,a, b)	for(ll i = a; i <= b; i ++)
#define rep(i, n)	for(ll i = 0; i < n; i++)
#define rv(i, a, b)	for(ll i = a; i >=b;i--)

pair<ll, ll> split(ll x){
	return make_pair((x-1)/2, x/2);
}

void solve(){
	map<ll,ll> mm;
	ll n, k;	cin>>n>>k;
	mm[n] = 1;
	pair<ll, ll> temp;
	while(k){
		pair<ll, ll> foo;
		foo.first = mm.rbegin()->first;
		foo.second = mm.rbegin()->second;
		ll val = min(foo.second, k);
		k-=val;
		foo.second-=val;
		if(foo.second==0)	mm.erase(foo.first);
		temp = split(foo.first);
		mm[temp.first]+=val;
		mm[temp.second]+=val;
		if(k==0)	break;
	}
	cout<<temp.second<<' '<<temp.first<<'\n';
}

int main(){
	ios_base::sync_with_stdio(0);	cin.tie();
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;	cin>>t;
	for(ll i =1; i <=t; i ++){
		cout<<"Case #"<<i<<": ";
		solve();
	}
}