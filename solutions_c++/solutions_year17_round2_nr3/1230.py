#include <bits/stdc++.h>

using namespace std;

double solve()
{
	long long n, q;
	cin >> n >> q;

	vector<long long> e(n);
	vector<long long> s(n);
	for (int i = 0; i < n; i++) {
		cin >> e[i] >> s[i];
	}
	vector<vector<long long>> g(n, vector<long long>(n, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> g[i][j];
		}
	}
	for (int i = 0; i < q; i++) {
		int u, v;
		cin >> u >> v;
	}
	vector<double> ans(n, 1e40);
	ans[0] = 0;
	for (int i = 0; i < n - 1; i++) {
		int nxt = i + 1;
		long long nxt_dist = g[nxt - 1][nxt];
		double cost = 0.0;
		while (e[i] >= nxt_dist && nxt < n) {
			cost += (double)g[nxt - 1][nxt] / s[i];
			ans[nxt] = min(ans[nxt], ans[i] + cost);
			nxt++;
			if (nxt < n) nxt_dist += g[nxt - 1][nxt];
		}
	}
	return ans[n - 1];
}

int main()
{
	int t;
	cin >> t;
	cout << fixed << setprecision(6);
	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
