#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <map>

using namespace std;
#define kal pair <pair <int, int>, pair <int, int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
const int MAXN = 200;
const int INF = 1e9 + 7;

int solve() {
	int hd, ad, hk, ak, b, d;
	cin >> hd >> ad >> hk >> ak >> b >> d;
	int me = hd;
	map <kal, int> dp;
	kal kk = mp(mp(hd, ad), mp(hk, ak));
	dp[kk] = 0;
	queue <kal> q;
	q.push(kk);
	while (!q.empty()) {
		kal v = q.front();
		q.pop();
		hd = v.ff.ff, ad = v.ff.ss, hk = v.ss.ff, ak = v.ss.ss;
		if (ad >= hk) {
			return dp[v] + 1;
		} 
		if (hd > ak) {  // attack, buff
			kk = mp(mp(hd - ak, ad), mp(hk - ad, ak));
			if (dp.count(kk) == 0 || dp[kk] > 1 + dp[v]) {
				dp[kk] = 1 + dp[v];
				q.push(kk);
			}
			kk = mp(mp(hd - ak, ad + b), mp(hk, ak));
			if (dp.count(kk) == 0 || dp[kk] > 1 + dp[v]) {
				dp[kk] = 1 + dp[v];
				q.push(kk);
			}
		}
		if (me > ak) { //cure
			kk = mp(mp(me - ak, ad), mp(hk, ak));
			if (dp.count(kk) == 0 || dp[kk] > 1 + dp[v]) {
				dp[kk] = 1 + dp[v];
				q.push(kk);
			}
		}
		if (hd > max(0, ak - d)) { //debuff
			int nk = max(0, ak - d);
			kk = mp(mp(hd - nk, ad), mp(hk, nk));
			if (dp.count(kk) == 0 || dp[kk] > 1 + dp[v]) {
				dp[kk] = 1 + dp[v];
				q.push(kk);
			}
		}
	}
	return -1;
}

int32_t main() {
	freopen("testc.in", "r", stdin);
	freopen("testc.out", "w", stdout);
	int cc;
	cin >> cc;
	for (int i = 1; i <= cc; ++i) {
		int ans = solve();
		if (ans == -1) 
			cout << "Case #" << i << ": IMPOSSIBLE" << '\n';
		else
			cout << "Case #" << i << ": " << ans << '\n';
	}
}