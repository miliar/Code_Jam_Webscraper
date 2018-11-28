#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define ld double

using namespace std;

const int nm = 1450;
const int inf = 1e9;

int n[2];
int f[nm][nm][2][2];
bool busy[2][nm];

int dp(int s1, int s2, int cur, int first) {
	int &res = f[s1][s2][cur][first];
	if (res != -1) {
		return res;
	}
	int t = s1 + s2;
	if (t == 1440) {
		if (s1 != 720 || s2 != 720)
			res = inf;
		else if (cur == first)
			res = 0;
		else
			res = 1;
		return res;
	}
	res = inf;
	if (busy[0][t]) {
		res = dp(s1, s2 + 1, 1, first) + (cur != 1);
	} else if (busy[1][t]) {
		res = dp(s1 + 1, s2, 0, first) + (cur != 0);
	} else {
		res = min(dp(s1 + 1, s2, 0, first) + (cur != 0), dp(s1, s2 + 1, 1, first) + (cur != 1));
	}
	return res;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n[0] >> n[1];
	memset(busy, 0, sizeof(busy));
	for (int i = 0; i < 2; ++i) {
		for (int j = 1; j <= n[i]; ++j) {
			int l, r;
			cin >> l >> r;
			for (int k = l; k < r; ++k) {
				busy[i][k] = 1;
			}
		}
	}
	memset(f, -1, sizeof(f));
	int res = inf;
	if (!busy[0][0]) {
		res = dp(1, 0, 0, 0);
	}
	if (!busy[1][0]) {
		res = min(res, dp(0, 1, 1, 1));
	}
	cout << res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
//	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
