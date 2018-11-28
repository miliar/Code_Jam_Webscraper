#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

pair<ll, ll> solve() {
	ll n, k, sum = 1, curr[2] = {0, 0}, cnt[2] = {0, 0};
	cin >> n >> k;
	curr[n & 1] = n;
	cnt[n & 1] = 1;
	while((sum << 1)-1 < k) {
		ll tmp[2] = {0, 0};
		tmp[(curr[1] >> 1) & 1] += cnt[1] << 1;
		tmp[(curr[0] >> 1) & 1] += cnt[0];
		tmp[(curr[0] >> 1)-1 & 1] += cnt[0];
		cnt[0] = tmp[0];
		cnt[1] = tmp[1];
		if(curr[0]) {
			if((curr[0] >> 1) & 1) {
				curr[1] = curr[0] >> 1;
				curr[0] = (curr[0] >> 1)-1;
			} else {
				curr[1] = (curr[0] >> 1)-1;
				curr[0] = curr[0] >> 1;
			}
		} else curr[(curr[1] >> 1) & 1] = curr[1] >> 1;
		sum <<= 1;
	}
	// cout << sum-1 << ' ' << curr[0] << ' ' << curr[1] << ' ' << cnt[0] << ' ' << cnt[1] << endl;
	ll mn = min(curr[0], curr[1]), mx = max(curr[0], curr[1]);
	if(cnt[mx & 1] >= k-(sum-1)) {
		if(mx & 1) return {mx >> 1, mx >> 1};
		else return {mx >> 1, (mx >> 1)-1};
	} else {
		if(mn & 1) return {mn >> 1, mn >> 1};
		else return {mn >> 1, (mn >> 1)-1};
	}
}

int main() {
	freopen("out.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		auto res = solve();
		cout << "Case #" << i << ": " << res.first << ' ' << res.second << endl;
	}
}
