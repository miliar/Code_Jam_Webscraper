#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define PI 3.1415926535897932384626433

ll n, k;

int main() {
	ll T;
	cin >> T;
	for(int TT = 1; TT <= T; TT++) {
		ll C, J;
		ll ans = 2;
		vector<pair<ll,ll>> c, j;
		cin >> C >> J;

		for(int i = 0; i < C; i++) {
			ll x, y;
			cin >> x >> y;
			c.push_back({x, y});
		}
		for(int i = 0; i < J; i++) {
			ll x, y;
			cin >> x >> y;
			j.push_back({x, y});
		}

		if(C==2) {
//			cout << c[0].second << " " << c[1].second << " | " << c[0].first << " " << c[1].first << endl;
			if(max(c[0].second, c[1].second) - min(c[0].first, c[1].first) <= 720)
				ans = 2;
			else if(min(c[0].second, c[1].second) - max(c[0].first, c[1].first) + 1440 <= 720)
				ans = 2;
			else 
				ans = 4;
		} else if(J==2) {
			if(max(j[0].second, j[1].second) - min(j[0].first, j[1].first) <= 720)
				ans = 2;
			else if(min(j[0].second, j[1].second) - max(j[0].first, j[1].first) + 1440 <= 720)
				ans = 2;
			else
				ans = 4;
		} else if((C==1&&J==0)||(C==0&&J==1)) {
			ans = 2;
		} else {
			ans = 2;
		}


		cout << "Case #" << TT << ": " << fixed << ans << endl;
	}
}