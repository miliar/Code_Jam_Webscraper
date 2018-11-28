#include <bits/stdc++.h>
using namespace std;

map<vector<int>, int> f[4];
int p;

int dfs(int u, vector<int> &cnt) {
	if (f[u].count(cnt) == 1) {
		return f[u][cnt];
	}
	int &res = f[u][cnt];
	if (accumulate(cnt.begin() + 1, cnt.end(), 0) == 0) {
		return res = 0;
	}
	for (int i = 1; i < (int) cnt.size(); ++i) if (cnt[i] > 0) {
		--cnt[i];
		res = max(res, dfs((u + i) % p, cnt) + (u == 0 ? 1 : 0));
		++cnt[i];
	}
	return res;
}

int run() {
	int n; cin >> n >> p;
	vector<int> cnt (p, 0);
	for (int i = 0; i < n; ++i) {
		int x; cin >> x;
		++cnt[x % p];
	}
	for (int i = 0; i < p; ++i) f[i].clear();
	return dfs(0, cnt) + cnt[0];
}

int main() {
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) {
		cout << "Case #" << tc << ": " << run() << '\n';
	}
	cout << '\n';
}
