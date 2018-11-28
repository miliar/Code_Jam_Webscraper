#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

map<ll, ll> c;

ll get(ll n, ll li, int s){
	if (li==0) return n;
	if (s==0){
		if (n<li*2) return 0;
	}
	else{
		if (n<=li*2) return 0;
	}
	if (c.count(n)) return c[n];
	ll re=1;
	if (n%2==0){
		re+=get(n/2, li, s);
		re+=get(n/2-1, li, s);
	}
	else{
		re+=get(n/2, li, s);
		re+=get(n/2, li, s);
	}
	c[n]=re;
	return re;
}

void solve(){
	ll n,k;
	cin>>n>>k;
	ll mi=0;
	ll ma=1e18+10;
	while (mi<=ma){
		ll mid=(mi+ma)/2;
		c.clear();
		if (get(n, mid, 0)>=k){
			mi=mid+1;
		}
		else{
			ma=mid-1;
		}
	}
	cout<<ma<<" ";
	mi=0;
	ma=1e18+10;
	while (mi<=ma){
		ll mid=(mi+ma)/2;
		c.clear();
		if (get(n, mid, 1)>=k){
			mi=mid+1;
		}
		else{
			ma=mid-1;
		}
	}
	cout<<ma<<endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}