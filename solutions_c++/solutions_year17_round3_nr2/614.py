#include<cstdio>
#include<algorithm>
#include<limits.h>
#include<string>
#include<vector>
#include<functional>
#include<iostream>
#include<stdlib.h>
using namespace std;

bool a[1440], b[1440];
int dp[1441][1441][2];
signed main() {
	freopen("X.txt", "w", stdout);
	int c; cin >> c;
	for (int d = 0; d < c; d++) {
		memset(a, true, sizeof(a));
		memset(b, true, sizeof(b));
		int e, f; cin >> e >> f;
		for (int g = 0; g < e; g++) {
			int h, i; cin >> h >> i;
			while (h < i) {
				a[h] = false;
				h++;
			}
		}
		for (int g = 0; g < f; g++) {
			int h, i; cin >> h >> i;
			while (h < i) {
				b[h] = false;
				h++;
			}
		}
		int ans = 1 << 29;
		memset(dp, 0x3f, sizeof(dp));
		dp[0][0][0] = 0;
		for (int i = 0; i < 1440; i++) {
			for (int j = 0; j <= 730; j++) {
				//�ς��
				if (b[i]) {
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
				}
				//�ς��Ȃ�
				if (a[i]) {
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
				}
				//�ς��
				if (a[i]) {
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
				}
				//�ς��Ȃ�
				if (b[i]) {
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
				}
			}
		}
		ans = min(dp[1440][720][0], dp[1440][720][1] + 1);
		memset(dp, 0x3f, sizeof(dp));
		dp[0][0][1] = 0;
		for (int i = 0; i < 1440; i++) {
			for (int j = 0; j <= 730; j++) {
				//�ς��
				if (b[i]) {
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
				}
				//�ς��Ȃ�
				if (a[i]) {
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
				}
				//�ς��
				if (a[i]) {
					dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
				}
				//�ς��Ȃ�
				if (b[i]) {
					dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
				}
			}
		}
		ans = min({ dp[1440][720][1], dp[1440][720][0] + 1 ,ans });
		printf("Case #%d: %d\n", d + 1, ans);
	}
}