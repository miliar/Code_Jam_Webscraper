#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<double, int> ii;

ll md = 1e9+7;

int main() {
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		int n, k;
		cin >> n >> k;
		priority_queue<ii> pq;
		ll r[n];
		ll h[n];
		for (int i = 0; i < n; i++) {
			ll a, b; cin >> a >> b;
			r[i] = a;
			h[i] = b;
			pq.push(ii(2 * acos(-1) * a * b, i));
		}
		int cc = k-1;
		double ans = 0;
		bitset<1001> bs;
		ll cmax = 0, cbase = -1;
		while (cc) {
			ii top = pq.top(); pq.pop();
			ans += top.first;
			cc--;
			bs[top.second] = 1;
			if (cmax < r[top.second]) {
				cmax = r[top.second];
				cbase = top.second;
			}
		}

		if (k == 1) {
			
			for (int i = 0; i < n; i++) {
				double cans = 0;
				cans += acos(-1) * r[i] * r[i];
				cans += 2 * acos(-1) * r[i] * h[i];
				ans = max(ans, cans);
			}
			
		} else {
			double bans = ans;
			for (int i = 0; i < n; i++) {
				double cans = bans;
				if (!bs[i]) {
					if (r[cbase] < r[i]) {
						cans += acos(-1) * r[i] * r[i];
						cans += 2 * acos(-1) * r[i] * h[i];
					} else {
						cans += acos(-1) * r[cbase] * r[cbase];
						cans += 2 * acos(-1) * r[i] * h[i];
					}
					ans = max(cans, ans);
				}
			}
		}
		
		
		printf("Case #%d: %.6lf\n", t, ans);
	}

}