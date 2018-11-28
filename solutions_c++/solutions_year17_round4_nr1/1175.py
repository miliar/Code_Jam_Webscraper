#include <bits/stdc++.h>
using namespace std;

int dfs(vector<int> cnt, int reminder, vector<map<vector<int>, int>> &dp, const int p, int left) {
	if (!left) return 0;
	if (dp[reminder].find(cnt) != dp[reminder].end()) return dp[reminder][cnt];
  int ret = -1e8;
  for (int i = 0; i < cnt.size(); ++i) {
		if (cnt[i] == 0) continue;
		cnt[i]--;
    ret = max(ret, dfs(cnt, (i + reminder) % p, dp, p, left - 1) + ((i + reminder) % p == 0 || left == 1));
		cnt[i]++;
  }
	return dp[reminder][cnt] = ret;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int CAS, n, p, x;
	cin >> CAS;
	for (int cas = 1; cas <= CAS; cas++) {
		cin >> n >> p;
		vector<map<vector<int>, int>> dp(p, map<vector<int>, int>());
		vector<int> cnt(p, 0);
    for (int i = 0; i < n; i++) {
      cin >> x;
      cnt[x % p]++;
    }
    int temp = cnt[0];
		n -= cnt[0];
    cnt[0] = 0;
    printf("Case #%d: ", cas);
    cerr << cas << endl;
    cout << dfs(cnt, 0, dp, p, n) + temp << endl;
	}
}
