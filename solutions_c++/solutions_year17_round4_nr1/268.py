	//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

const int N = 111;

int a[N];

int n, p;

int b[5];

inline void solve2() {
	int dp[N][N][5];
	memset(dp, 0, sizeof(dp));
	dp[b[0]][b[1]][0] = 0;
	for (int i = b[0]; i >= 0; i--) {
		for (int j = b[1]; j >= 0; j--) {
			for (int k = 0; k < 2; k++) {
				if (i > 0) {
					dp[i - 1][j][k] = max(dp[i - 1][j][k], dp[i][j][k] + (!k));
				}
				if (j > 0) {
					dp[i][j - 1][(k ^ 1)] = max(dp[i][j - 1][(k ^ 1)], dp[i][j][k] + (!k));
				}
			}
		}
	}
	cout << max(dp[0][0][0], dp[0][0][1]) << endl;
}

int dp2[N][N][N][5];

inline void solve3() {
	memset(dp2, 0, sizeof(dp2));
	dp2[b[0]][b[1]][b[2]][0] = 0;
	for (int i = b[0]; i >= 0; i--) {
		for (int j = b[1]; j >= 0; j--) {
			for (int l = b[2]; l >= 0; l--) {
				for (int k = 0; k < 3; k++) {
					if (i > 0) {
						dp2[i - 1][j][l][k] = max(dp2[i - 1][j][l][k], dp2[i][j][l][k] + (!k));
					}
					if (j > 0) {
						dp2[i][j - 1][l][(k + 1) % 3] = max(dp2[i][j - 1][l][(k + 1) % 3], dp2[i][j][l][k] + (!k));
					}
					if (l > 0) {
						dp2[i][j][l - 1][(k + 2) % 3] = max(dp2[i][j][l - 1][(k + 2) % 3], dp2[i][j][l][k] + (!k));
					}
				}
			}
		}
	}
	cout << max(dp2[0][0][0][0], max(dp2[0][0][0][1], dp2[0][0][0][2])) << endl;
}

int dp[2][N][N][N][5];

inline void solve4() {
	int used[2][N][N][N][5];
	memset(dp, 0, sizeof(dp));
	memset(used, 0, sizeof(used));
	dp[0][b[0]][b[1]][b[2]][0] = 1;
	int id = 0, cnt;
	for (int it = 0; it < n; it++) {
		for (int i = b[0]; i >= 0; i--) {
			for (int j = b[1]; j >= 0; j--) {
				for (int l = b[2]; l >= 0; l--) {
					for (int k = 0; k < 4; k++) {
						if (i > 0) {
							if (used[(id ^ 1)][i - 1][j][l][k] != it + 1) {
								used[(id ^ 1)][i - 1][j][l][k] = it + 1;
								dp[(id ^ 1)][i - 1][j][l][k] = 0;
							}
							dp[(id ^ 1)][i - 1][j][l][k] = max(dp[(id ^ 1)][i - 1][j][l][k], dp[id][i][j][l][k] + (!k));
						}
						if (j > 0) {
							if (used[(id ^ 1)][i][j - 1][l][(k + 1) % 4] != it + 1) {
								used[(id ^ 1)][i][j - 1][l][(k + 1) % 4] = it + 1;
								dp[(id ^ 1)][i][j - 1][l][(k + 1) % 4] = 0;
							}
							dp[(id ^ 1)][i][j - 1][l][(k + 1) % 4] = max(dp[(id ^ 1)][i][j - 1][l][(k + 1) % 4], dp[id][i][j][l][k] + (!k));
						}
						if (l > 0) {
							if (used[(id ^ 1)][i][j][l - 1][(k + 2) % 4] != it + 1) {
								used[(id ^ 1)][i][j][l - 1][(k + 2) % 4] = it + 1;
								dp[(id ^ 1)][i][j][l - 1][(k + 2) % 4] = 0;
							}
							dp[(id ^ 1)][i][j][l - 1][(k + 2) % 4] = max(dp[(id ^ 1)][i][j][l - 1][(k + 2) % 4], dp[id][i][j][l][k] + (!k));
						}
						cnt = it - (b[0] - i) + (b[1] - j) + (b[2] - l);
						if (cnt < b[3]) {
							if (used[(id ^ 1)][i][j][l][(k + 3) % 4] != it + 1) {
								used[(id ^ 1)][i][j][l][(k + 3) % 4] = it + 1;
								dp[(id ^ 1)][i][j][l][(k + 3) % 4] = 0;
							}
							dp[(id ^ 1)][i][j][l][(k + 3) % 4] = max(dp[(id ^ 1)][i][j][l][(k + 3) % 4], dp[id][i][j][l][k] + (!k));
						}
					}
				}
			}
		}
		id ^= 1;
	}
	int ans = 0;
	if (used[n % 2][0][0][0][0] == n) {
		ans = dp[n % 2][0][0][0][0];
	}
	if (used[n % 2][0][0][0][1] == n) {
		ans = max(ans, dp[n % 2][0][0][0][1]);
	}
	if (used[n % 2][0][0][0][2] == n) {
		ans = dp[n % 2][0][0][0][2];
	}
	if (used[n % 2][0][0][0][3] == n) {
		ans = max(ans, dp[n % 2][0][0][0][3]);
	}
	cout << ans << endl;
}


inline void solve() {
	cin >> n >> p;
	memset(b, 0, sizeof(b));
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		b[a[i] % p]++;
	}
	if (p == 2) {
		solve2();
	}
	if (p == 3) {
		solve3();
	}
	if (p == 4) {
		solve4();
	}
}	

int main() {
	freopen (fname"A-small-attempt1.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
