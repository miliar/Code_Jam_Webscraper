#include<cstdio>
#define day_time 1440

int t, ac, aj, c, d, j, k, u[1441], v[1441]; // u[i] -> (i, i+1)
int dp[1441][721][2]; // dp[time][by_C][is_C]

int max(int x, int y) {
	return x > y ? x : y;
}

int min(int x, int y) {
	return x < y ? x : y;
}

int rnd(int x) {
	return x + x % 2;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%d %d", &ac, &aj);
		u[0] = v[0] = 1;
		for (int i = 1; i < day_time; i++) u[i] = v[i] = 0;
		for (int i = 0; i < ac; i++) {
			scanf("%d %d", &c, &d);
			u[c] -= 1;
			u[d] += 1;
		}
		for (int i = 0; i < aj; i++) {
			scanf("%d %d", &j, &k);
			v[j] -= 1;
			v[k] += 1;
		}
		for (int i = 1; i < day_time; i++) u[i] += u[i - 1], v[i] += v[i - 1];
		for (j = 1; j <= day_time/2; j++) dp[0][j][0] = dp[0][j][1] = 2000;
		for (int i = 1; i <= day_time; i++) {
			if (u[i - 1]) dp[i][0][1] = dp[i - 1][0][0] + 1;
			else dp[i][0][1] = 2000;
			if (v[i - 1]) dp[i][0][0] = dp[i - 1][0][0];
			else dp[i][0][0] = 2000;
			for (int j = 1; j <= day_time/2; j++) {
				dp[i][j][0] = dp[i][j][1] = 2000;
				if (u[i - 1]) dp[i][j][1] = min(dp[i - 1][j - 1][1], dp[i - 1][j][0] + 1);
				if (v[i - 1]) dp[i][j][0] = min(dp[i - 1][j - 1][1] + 1, dp[i - 1][j][0]);
			}
		}
		printf("Case #%d: %d\n", test, rnd(min(dp[day_time][day_time/2][0], dp[day_time][day_time/2][1])));
	}
}
