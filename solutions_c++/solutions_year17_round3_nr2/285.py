#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iostream>

using namespace std;

const int maxn = 1500;

int T, n, m, a, b, t[maxn];
int dp[maxn][maxn][2], res;

int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("B3.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> n >> m;
		memset(t, 0, sizeof(t));
		for(int i = 0; i < n; i ++) {
			cin >> a >> b;
			for(int j = a; j < b; j ++) t[j] = 1;
		}
		for(int i = 0; i < m; i ++) {
			cin >> a >> b;
			for(int j = a; j < b; j ++) t[j] = 2;
		}
		
		int L = 720;
		res = maxn;

		memset(dp, 63, sizeof(dp));
		dp[0][0][0] = 0;
		for(int i = 0; i <= L; i ++) for(int j = 0; j <= L; j ++) {
			int now = i+j;
			if(t[now] != 1) {
				dp[i+1][j][0] = min(dp[i][j][0], dp[i][j][1] + 1);
			}
			if(t[now] != 2) {
				dp[i][j+1][1] = min(dp[i][j][0] + 1, dp[i][j][1]);
			}
		}
		res = min(res, min(dp[L][L][0], dp[L][L][1] + 1));

		memset(dp, 63, sizeof(dp));
		dp[0][0][1] = 0;
		for(int i = 0; i <= L; i ++) for(int j = 0; j <= L; j ++) {
			int now = i+j;
			if(t[now] != 1) {
				dp[i+1][j][0] = min(dp[i][j][0], dp[i][j][1] + 1);
			}
			if(t[now] != 2) {
				dp[i][j+1][1] = min(dp[i][j][0] + 1, dp[i][j][1]);
			}
		}
		res = min(res, min(dp[L][L][0] + 1, dp[L][L][1]));
		
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}

