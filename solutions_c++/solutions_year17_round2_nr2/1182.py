#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
int cnt[10];
inline void solve() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%d", &cnt[i]);
	}
	vector <pair <int, char> > v;
	v.pb(mp(cnt[0], 'R'));
	v.pb(mp(cnt[2], 'Y'));
	v.pb(mp(cnt[4], 'B'));
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	string ans;
	for (int i = 1; i <= v[0].first; i++) {
		ans += v[0].second;
		if (v[1].first) {
			ans += v[1].second;
			v[1].first--;
		} else if (v[2].first) {
			ans += v[2].second;
			v[2].first--;
		} else {

			cout <<  "IMPOSSIBLE\n";
			return;
		}
	}
	string ans2;
	ans2 += ans[0];
	for (int i = 1;  i  < ans.size(); i++) {
		char last = ans2[(int)ans2.size() - 1];
		if (v[2].first > 0 && last != v[2].second && ans[i] != v[2].second) {
			ans2 += v[2].second;
			ans2 += ans[i];
			v[2].first--;
		} else {
			ans2 += ans[i];

		}
	}
	if (ans2.size() != n) {
		cout << "IMPOSSIBLE\n";
	} else {
		for (int i = 1; i < n; i++) {
			if (ans2[i] == ans2[i - 1] || ans2[n - 1] == ans2[0]) {
				cout << "IMPOSSIBLE\n";
				return;
			}
		}
		cout << ans2 << endl;
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		solve();
	}
}
