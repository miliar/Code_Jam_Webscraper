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
		cin >> n >> k;
		ld ans = 0;
		vector<ll> r, h;
		vector<pair<ld, ll>> curSur;
		vector<pair<ld,ll>> result;
		bool used[1005];
		memset(used, 0, sizeof(used));

		for(int i = 0; i < n; i++) {
			ll R, H;
			cin >> R >> H;
			r.push_back(R);
			h.push_back(H);
			curSur.push_back({2.*PI*R*H, i});
		}

		sort(curSur.rbegin(), curSur.rend());


		ll maxR = 0;
		for(int i = 0; i < k-1; i++) {
			ans += curSur[i].first;
//			cout << ans << endl;
			used[curSur[i].second] = 1;
			maxR = max(maxR, r[curSur[i].second]);
		}

		ld oldAns = ans;
		ans += (ld)maxR*(ld)maxR*PI;
//		cout << ans << "\t" << oldAns << endl;
		for(int i = 0; i < n; i++) {
			if(!used[i]) {
				ll R = r[i];
				ll H = h[i];
				ans = max(ans, oldAns + 2.*PI*R*H + (ld)max(maxR, R)*(ld)max(maxR, R)*PI);
			}
		}

		cout << setprecision(14);
		cout << "Case #" << TT << ": " << fixed << ans << endl;
//		cout << endl;
	}
}