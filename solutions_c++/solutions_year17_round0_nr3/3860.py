#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;
int ans1, ans2;
const int MAXN = 1e6 + 20;
int am[MAXN];


void solve() {
	for (int i = 0; i < MAXN; ++i)
		am[i] = 0;
	int n, k;
	cin >> n >> k;
	am[n]++;
	int cnt = n;
	for (int i = 0; i + 1 < k; ++i) {
		while (am[cnt] == 0)
			cnt--;
		am[cnt]--;
		am[cnt / 2]++;
		am[(cnt - 1) / 2]++;
	}
	while (am[cnt] == 0)
		cnt--;
	ans1 = cnt / 2;
	ans2 = (cnt - 1) / 2;
}

int main() {
	freopen("testc2.in", "r", stdin);
	freopen("testc2.out", "w", stdout);
	int cc;
	cin >> cc;
	for (int i = 1; i <= cc; ++i) {
		solve();
		cout << "Case #" << i << ": " << ans1 << ' ' << ans2 << '\n';
	}
}