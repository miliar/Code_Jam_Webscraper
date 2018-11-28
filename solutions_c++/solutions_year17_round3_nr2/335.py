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

const int maxn = 1500;

int dp[2][2][maxn][maxn];

int a[maxn];

inline void solve() {
	int aC, aJ;
	cin >> aC >> aJ;
	int l, r;
	memset(a, -1, sizeof(a));
	for (int i = 1; i <= aC; i++) {
		cin >> l >> r;
		for (int j = l; j < r; j++) {
			a[j] = 0;
		}
	}
	for (int i = 1; i <= aJ; i++) {
		cin >> l >> r;
		for (int j = l; j < r; j++) {
			a[j] = 1;
		}
	}
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int c = 0; c < 2; c++) {
				for (int k = 0; k < 2; k++) {
					dp[i][j][c][k] = inf;
				}
			}
		}
	}
	if (a[0] == -1) {
		dp[0][0][0][1] = dp[1][1][0][0] = 0;
	}
	else if (a[0] == 0) {
		dp[0][0][0][1] = 0;
	}
	else {
		dp[1][1][0][0] = 0;
	}
	for (int i = 1; i < 1440; i++) {
		for (int c = 0; c <= min(i + 1, 720); c++) {
			for (int k = 0; k < 2; k++) {
				for (int init = 0; init < 2; init++) {
					if (a[i] == 1 - k) {
						dp[init][k][i][c] = inf;
					}
					else {
						if (!k) {
							if (c) {
								dp[init][k][i][c] = inf;
								dp[init][k][i][c] = min(dp[init][k][i - 1][c - 1], dp[init][k][i][c]);
								dp[init][k][i][c] = min(dp[init][1][i - 1][c - 1] + 1, dp[init][k][i][c]);
							}
						}
						else {
							dp[init][k][i][c] = inf;
							dp[init][k][i][c] = min(dp[init][k][i - 1][c], dp[init][k][i][c]);
							dp[init][k][i][c] = min(dp[init][0][i - 1][c] + 1, dp[init][k][i][c]);
						}
					}
/*					if (dp[init][k][i][c] < 3) {
						cout << init << " " << k << " " << i << " " << c << " " << dp[init][k][i][c] << endl;
					}
*/				}
			}
		}
	}
	int ans = inf;
	for (int init = 0; init < 2; init++) {
		for (int k = 0; k < 2; k++) {
//			cout << init << " " << k << " " << dp[init][k][1439][720] << endl;
			if (k == init) {		
				ans = min(ans, dp[init][k][1439][720]);			
			}
			else {
				ans = min(ans, dp[init][k][1439][720] + 1);			
			}
		}
	}
	cout << ans << endl;
}

int main() {
	freopen (fname"B-large.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j <= 1440; j++) {
			for (int k = 0; k <= 1440; k++) {
				dp[0][i][j][k] = dp[1][i][j][k] = inf;
			}
		}
	}
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
