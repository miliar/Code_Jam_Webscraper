#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 101;

int n, p, stamp, vis[N][N][N][N], dp[N][N][N][N], cnt[4];

int getAns(int a, int b, int c, int d, int sum) {
	if (!(a + b + c + d)) {
		return 0;
	}
	if (vis[a][b][c][d] == stamp) {
		return dp[a][b][c][d];
	}
	vis[a][b][c][d] = stamp;
	int &tmp = dp[a][b][c][d], delta = sum % p ? 0 : 1;
	tmp = 0;
	if (a) {
		tmp = max(tmp, getAns(a - 1, b, c, d, sum + 0));
	}
	if (b) {
		tmp = max(tmp, getAns(a, b - 1, c, d, sum + 1));
	}
	if (c) {
		tmp = max(tmp, getAns(a, b, c - 1, d, sum + 2));
	}
	if (d) {
		tmp = max(tmp, getAns(a, b, c, d - 1, sum + 3));
	}
	tmp += delta;
	return tmp;
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		memset(cnt, 0, sizeof(cnt));
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; ++i) {
			int a;
			scanf("%d", &a);
			cnt[a % p]++;
		}
		++stamp;
		static int id = 0;
		printf("Case #%d: %d\n", ++id, getAns(cnt[0], cnt[1], cnt[2], cnt[3], 0));
	}
	return 0;
}
