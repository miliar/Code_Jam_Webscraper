#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXN = 733;
int f[MAXN][MAXN][2][2];
int act[MAXN*2];

void upd(int &a, int b) {
	if (b < a) a = b;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T; cin >> T;
	for (int kase = 1; kase <= T; ++kase) {
		int Ac, Aj; cin >> Ac >> Aj;
		memset(act, 0, sizeof act);
		for (int i = 0; i < Ac; ++i) {
			int c, d; cin >> c >> d;
			for (int j = c + 1; j <= d; ++j)
				act[j] = 1;
		}
		for (int i = 0; i < Aj; ++i) {
			int c, d; cin >> c >> d;
			for (int j = c + 1; j <= d; ++j)
				act[j] = 2;
		}
		memset(f, 0x3f, sizeof f);
		f[0][0][0][0] = f[0][0][1][1] = 0;
		f[0][0][0][1] = f[0][0][1][0] = 1;
		for (int i = 1; i <= 1440; ++i) {
			for (int j = 0; j <= min(i, 720); ++j) {
				int k = i - j;
				if (k > 720) continue;
				//	cout << i << ' ' << k << ' ' << j << endl;
				if (act[i] == 1 && k >= 1) {
					upd(f[k][j][0][0], f[k - 1][j][0][1] + 1);
					upd(f[k][j][0][0], f[k - 1][j][0][0]);
					upd(f[k][j][1][0], f[k - 1][j][1][1] + 1);
					upd(f[k][j][1][0], f[k - 1][j][1][0]);
				}
				if (act[i] == 2 && j >= 1) {
					upd(f[k][j][0][1], f[k][j - 1][0][1]);
					upd(f[k][j][0][1], f[k][j - 1][0][0] + 1);
					upd(f[k][j][1][1], f[k][j - 1][1][1]);
					upd(f[k][j][1][1], f[k][j - 1][1][0] + 1);
				}
				if (act[i] == 0) {
					if (k >= 1) {
						upd(f[k][j][0][0], f[k - 1][j][0][0]);
						upd(f[k][j][0][0], f[k - 1][j][0][1] + 1);
						upd(f[k][j][1][0], f[k - 1][j][1][0]);
						upd(f[k][j][1][0], f[k - 1][j][1][1] + 1);
					}
					if (j >= 1) {
						upd(f[k][j][0][1], f[k][j - 1][0][0] + 1);
						upd(f[k][j][0][1], f[k][j - 1][0][1]);
						upd(f[k][j][1][1], f[k][j - 1][1][0] + 1);
						upd(f[k][j][1][1], f[k][j - 1][1][1]);
					}
				}
			}
		}
		int ans = 0x3f3f3f3f;
		ans = min(ans, f[720][720][0][0]);
		ans = min(ans, f[720][720][1][1]);
		ans = min(ans, f[720][720][1][0] + 1);
		ans = min(ans, f[720][720][0][1] + 1);
		cout << "Case #" << kase << ": " << ans << endl;
	}

	return 0;
}
