#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(ll i = a; i < ll(b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (ll)(x).size()
#define D(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<ll> vi;

double PI = 3.14159265358979;

int main() {
    cin.sync_with_stdio(false);
	ll t; cin>>t;
	ll Case = 1;
	while(t--) {
		ll n,k;
		cin>>n>>k;
		--k;
		vector<pair<double,ll> > pancakes(n);
		rep(i,0,n) {
			ll radius,height;
			cin>>radius>>height;
			pancakes[i].first = radius*2*PI*height;
			pancakes[i].second = radius;
		}
		sort(pancakes.begin(),pancakes.end());
		reverse(pancakes.begin(),pancakes.end());
		double mx = 0;
		rep(i,0,n){
			ll r = pancakes[i].second;
			double hArea = pancakes[i].first;
			ll num = 0;
			rep(j,0,n){
				if(num==k) break;
				if(pancakes[j].second<=r&&i!=j){
					hArea += pancakes[j].first;
					++num;
				}
			}
			mx = max(mx,r*r*PI + hArea);
		}
		cout<<"Case #"<<Case++<<": "<<fixed<<setprecision(10)<<mx<<endl;
	}
}