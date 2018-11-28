#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int main() {
	ll tt;
	cin>>tt;
	for(ll xx = 1; xx <= tt; ++xx) {
		cout<<"Case #"<<xx<<": ";
		ll n,k;
		cin>>n>>k;
		vector<pair<ll, ll> > v;
		v.push_back({n, 1});
		while(k) {
			sort(v.begin(), v.end());
			while(v.size() > 1 && v.back().first == v[v.size()-2].first) {
				v[v.size()-2].second += v.back().second;
				v.pop_back();
			}
			auto x = v.back();
			v.pop_back();
			if(k > x.second) {
				k -= x.second;
				v.push_back({(x.first-1)/2, x.second});
				v.push_back({x.first-1-(x.first-1)/2, x.second});
			}
			else {
				ll l = (x.first-1)/2;
				ll r = x.first-1-(x.first-1)/2;
				cout<<max(l, r)<<' '<<min(l, r)<<endl;
				break;
			}
		}
	}
}
