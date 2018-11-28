#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int MAXN = 110;
const int INF = 0x3f3f3f3f;

int G[MAXN];
int opt[MAXN][MAXN][MAXN];

void clear() {
	memset(G, 0, sizeof G);
	memset(opt, 0, sizeof opt);
}

int get_2(int cnt) {
	return (cnt + 1) / 2;
}

int get_3(int cnt) {
	int mod1 = 0, mod2 = 0;
	for (int i = 0; i < cnt; i++) {
		mod1 += (G[i] == 1);
		mod2 += (G[i] == 2);
	}
	int minv = min(mod1, mod2);
	mod1 -= minv;
	mod2 -= minv;
	return minv + (mod1 + 2) / 3 + (mod2 + 2) / 3;
}

int get_4(int cnt) {
	int mod1 = 0, mod2 = 0, mod3 = 0;
	for (int i = 0; i < cnt; i++) {
		mod1 += (G[i] == 1);
		mod2 += (G[i] == 2);
		mod3 += (G[i] == 3);
	}
	// cout << mod1 << " " << mod2 << " " << mod3 << endl;
	opt[1][0][0] = 1;
	opt[0][0][1] = 1;
	opt[0][1][0] = 1;
	opt[1][1][0] = 1;
	opt[0][1][1] = 1;
	opt[1][0][1] = 1;
	for (int i = 1; i <= 4; i++) {
		opt[i][0][0] = opt[0][0][i] = opt[0][i][0] = 1;
	}
	for (int i = 0; i <= mod1; i++) {
		for (int j = 0; j <= mod2; j++) {
			for (int k = 0; k <= mod3; k++) {
				int maxv = opt[i][j][k];
				if (i > 0 && k > 0) {
					maxv = max(maxv, opt[i - 1][j][k - 1] + 1);
				}
				if (j > 1) {
					maxv = max(maxv, opt[i][j - 2][k] + 1);
				}
				if (j > 0 && k > 1) {
					maxv = max(maxv, opt[i][j - 1][k - 2] + 1);
				}
				if (i > 1 && j > 0) {
					maxv = max(maxv, opt[i - 2][j - 1][k] + 1);
				}
				if (i > 3) {
					maxv = max(maxv, opt[i - 4][j][k] + 1);
				}
				if (j > 3) {
					maxv = max(maxv, opt[i][j - 4][k] + 1);
				}
				if (k > 3) {
					maxv = max(maxv, opt[i][j][k - 4] + 1);
				}
				opt[i][j][k] = maxv;
				// cout << "opt[" << i << "][" << j << "][" << k << "]" << " = " << opt[i][j][k] << endl;
			}
		}
	}
	return opt[mod1][mod2][mod3];
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	ios_base::sync_with_stdio(false);

	int T; cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		clear();
		int N, P; cin >> N >> P;
		int ret = 0;
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			int g; cin >> g;
			if ((g % P) == 0) {
				ret++;
			} else {
				G[cnt++] = g % P;
			}
		}
		if (P == 2) {
			ret += get_2(cnt);
		} else if (P == 3) {
			ret += get_3(cnt);
		} else {
			ret += get_4(cnt);
		}
		cout << "Case #" << kase << ": " << ret << endl;
	}
  return 0;
}