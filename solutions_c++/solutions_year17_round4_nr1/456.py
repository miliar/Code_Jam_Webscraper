#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 105;

int n, p, a[MAXN], f3[MAXN][MAXN], f4[MAXN][MAXN][MAXN], num[4];

int solve2() {
	return num[0] + num[1] / 2;
}

int solve3() {
	memset(f3, 200, sizeof f3);
	f3[num[1]][num[2]] = 0;
	for (int i = num[1]; i + 1; i --)
		for (int j = num[2]; j + 1; j --) {
			if (i + j == 0) continue;
			if (f3[i][j] < 0) continue;
			int sum = ((num[1] - i) + (num[2] - j) * 2) % 3;
			if (i) 
				f3[i - 1][j] = max(f3[i - 1][j], f3[i][j] + ((sum + 1) % 3 == 0));
			if (j)
				f3[i][j - 1] = max(f3[i][j - 1], f3[i][j] + ((sum + 2) % 3 == 0));
		}
	return f3[0][0] + num[0];
}

int solve4() {
	memset(f4, 200, sizeof f4);
	f4[num[1]][num[2]][num[3]] = 0;
	for (int i = num[1]; i + 1; i --)
		for (int j = num[2]; j + 1; j --) 
			for (int k = num[3]; k + 1; k --) {
				if (i + j + k == 0) continue;
				if (f4[i][j][k] < 0) continue;
				int sum = ((num[1] - i) + (num[2] - j) * 2 + (num[3] - k) * 3) % 4;
				if (i) 
					f4[i - 1][j][k] = max(f4[i - 1][j][k], f4[i][j][k] + ((sum + 1) % 4 == 0));
				if (j)
					f4[i][j - 1][k] = max(f4[i][j - 1][k], f4[i][j][k] + ((sum + 2) % 4 == 0));
				if (k)
					f4[i][j][k - 1] = max(f4[i][j][k - 1], f4[i][j][k] + ((sum + 3) % 4 == 0));
			}
	return f4[0][0][0] + num[0];
}

void solve(int tim) {
	printf("Case #%d: ", tim);
	scanf("%d%d", &n, &p);
	memset(num, 0, sizeof num);
	for (int i = 1; i <= n; i ++) {
		scanf("%d", &a[i]);
		num[a[i] % p] ++; 
	}
	if (p == 2) {
		int ans = 0;
		for (int i = 0; i < 2; i ++)
			if (num[i]) num[i] --, ans = max(ans, solve2()), num[i] ++;
		printf("%d\n", ans + 1);
	}
	if (p == 3) {
		int ans = 0;
		for (int i = 0; i < 3; i ++)
			if (num[i]) num[i] --, ans = max(ans, solve3()), num[i] ++;
		printf("%d\n", ans + 1);
	}
	if (p == 4) {
		int ans = 0;
		for (int i = 0; i < 4; i ++)
			if (num[i]) num[i] --, ans = max(ans, solve4()), num[i] ++;
		printf("%d\n", ans + 1);
	}
}

int main() {
	//freopen("data.in", "r", stdin), freopen("data.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}