#include <bits/stdc++.h>
using namespace std;

int sum[1111], cnt[1111];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T; cin >> T;
	for (int ks = 1; ks <= T; ++ks) {
		
		int n, m, c; cin >> n >> c >> m;
		int ans1, ans2;
		memset(cnt, 0, sizeof cnt);
		memset(sum, 0, sizeof sum);
		for (int i = 0; i < m; ++i) {
			int p, q; cin >> p >> q;
			++cnt[q];
			++sum[p];
		}
		for (int i = 1; i <= n; ++i)
			sum[i] += sum[i - 1];
		ans1 = cnt[1];
		for (int i = 1; i <= c; ++i)
			ans1 = max(ans1, cnt[i]);
		for (int i = 1; i <= n; ++i)
			ans1 = max(ans1, (sum[i] + i - 1) / i);
		ans2 = 0;
		for (int i = 1; i <= n; ++i)
			ans2 += max(0, (sum[i] - sum[i - 1]) - ans1);
		
		cout << "Case #" << ks << ": " << ans1 << ' ' << ans2 << endl;
	}

	return 0;
}
