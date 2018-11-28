#include <bits/stdc++.h>

using namespace std;
using ll = long long;

map< ll, ll, greater<ll> > pos;

pair<ll, ll> solve() {
	
	ll n, k;
	cin >> n >> k;
	pos.clear();
	pos[n] = 1;
	k--;

	while (k > 0) {
		ll at, cnt;
		tie(at, cnt) = *pos.begin();
		pos.erase(pos.begin());

		if (pos.find((at-1) / 2) == pos.end()) {
			pos[(at-1) / 2] = 0;
		}
		if (pos.find(at/2) == pos.end()) {
			pos[at/2] = 0;
		}
		pos[(at-1) / 2] += min(k, cnt);
		pos[at/2] += min(k, cnt);

		if (cnt <= k) {
			k -= cnt;
		} else {
			pos[at] = cnt - k;
			k = 0;
		}
	}

	ll res;
	tie(res, ignore) = *pos.begin();

	return make_pair(res/2, (res-1) / 2);
}

void report(int test_num, pair<ll, ll> ans) {
	printf("Case #%d: %" PRId64 " %" PRId64 "\n", test_num, ans.first, ans.second);
}

int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); 

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		report(i+1, solve());
	}

	return 0;
}