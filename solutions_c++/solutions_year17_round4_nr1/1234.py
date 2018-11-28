#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, P; cin >> N >> P;
		vector<int> G(P);
		for (int i = 0; i < N; i++) {
			int k; cin >> k;
			G[k % P]++;
		}
		int ans = 0;
		ans += G[0];
		if (P == 2) {
			ans += (G[1]+1) / 2;
		} else if (P == 3) {
			ans += min(G[1], G[2]);
			int left = max(G[1], G[2]) - min(G[1], G[2]);
			ans += (left+2) / 3;
		} else if (P == 4) {
			ans += G[2] / 2;
			ans += min(G[1], G[3]);
			int left = max(G[1], G[3]) - min(G[1], G[3]);
			ans += (left+3 + (G[2] % 2 ? 2 : 0)) / 4;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}