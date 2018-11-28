#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

using namespace std;
using big = long long;

const int MOD = 1000000007;

const int inf = 0x3f3f3f3f;


int n, m;

const int N = 120;
int f2[N][N], f3[N][N][N], f4[N][N][N][N];

inline void cmax(int &x, int y) {
	if (x < y) {
		x = y;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		vector<int> a;
		vector<int> cnt(4);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			++cnt[x % m];
			a.pb(x);
		}
		int ans = 0;
		if (m == 2) {
			memset(f2, -127, sizeof(f2));
			f2[0][0] = 0;
			for (int i = 0; i <= cnt[0]; ++i) {
				for (int j = 0; j <= cnt[1]; ++j) {
					int left = (m - j % m) % m;
					int w = f2[i][j];
					w += !left;
					cmax(f2[i][j + 1], w);
					cmax(f2[i + 1][j], w);
				}
			}
			ans = f2[cnt[0]][cnt[1]];
		} else if (m == 3) {
			memset(f3, -127, sizeof(f3));
			f3[0][0][0] = 0;
			for (int i = 0; i <= cnt[0]; ++i) {
				for (int j = 0; j <= cnt[1]; ++j) {
					for (int k = 0; k <= cnt[2]; ++k) {
						int left = (m - (j + k * 2) % m) % m;
						int w = f3[i][j][k];
						w += !left;
						cmax(f3[i + 1][j][k], w);
						cmax(f3[i][j + 1][k], w);
						cmax(f3[i][j][k + 1], w);
					}
				}
			}
			ans = f3[cnt[0]][cnt[1]][cnt[2]];
		} else if (m == 4) {
			memset(f4, -127, sizeof(f3));
			f4[0][0][0][0] = 0;
			for (int i = 0; i <= cnt[0]; ++i) {
				for (int j = 0; j <= cnt[1]; ++j) {
					for (int k = 0; k <= cnt[2]; ++k) {
						for (int p = 0; p <= cnt[3]; ++p) {
							int left = (m - (j + k * 2 + p * 3) % m) % m;
							int w = f4[i][j][k][p];
							w += !left;
							cmax(f4[i + 1][j][k][p], w);
							cmax(f4[i][j + 1][k][p], w);
							cmax(f4[i][j][k + 1][p], w);
							cmax(f4[i][j][k][p + 1], w);
						}
					}
				}
			}
			ans = f4[cnt[0]][cnt[1]][cnt[2]][cnt[3]];
		}
		printf("%d\n", ans);
	}
}
