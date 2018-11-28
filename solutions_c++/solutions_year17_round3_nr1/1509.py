#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


bool cmp(const pair<ll, ll> &l, const pair<ll, ll> &r) {
	ll l1 = l.first * l.second;
	ll r1 = r.first * r.second;
	if(l1 > r1) return true;
	return false;
}


int main() {
	int T;
	cin >> T;
	const double PI = (double) 3.141592653589;
	for(int _t = 1; _t <= T; _t++) {
		int n,k;
		cin >> n >> k;
		ll r, h;
		vector< pair<ll, ll> > v(n);
		for(int i=0; i<n; i++) {
			cin >> r >> h;
			v[i] = make_pair(r, h);
		}
		
		sort(v.begin(), v.end(), cmp);
		
		ll mr = -1;
		ll mh = -1;
		for(int i=0; i<n; i++) {
		//	cout << i << " " << v[i].first << " " << v[i].second << endl;
			if(mr < v[i].first) { mr = v[i].first; mh = v[i].second; }
			if(mr == v[i].first && mh < v[i].second) { mh = v[i].second; }
		}
		
		//cout << mr << " "<< mh << endl;
		bool flag = false;
		
		double ans = 0;
		
		ll mr2 = -1, mh2 = -1;
		for(int i=0; i<k; i++) {
		//	cout << v[i].first << " " << v[i].second << endl;
			if(mr2 < v[i].first) { mr2 = v[i].first; mh2 = v[i].second; }
			if(mr2 == v[i].first && mh2 < v[i].second) mh2 = v[i].second; //not required actually
			
			ans += 2*PI*v[i].first * v[i].second;
			if(v[i].first == mr) {
				flag = true;
			}
		}
		
		if(flag) {
			ans += PI*mr2*mr2;
		}
		else {
			ans += PI*mr2*mr2;
			
			ans = max(ans, ans - 2*PI*v[k-1].first * v[k-1].second - PI*mr2*mr2 + PI*mr*mr + 2*PI*mr*mh);
		}
		
		printf("Case #%d: %.8lf\n", _t, ans);
		
	}
	return 0;
}
