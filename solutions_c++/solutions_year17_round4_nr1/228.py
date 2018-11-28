#include <bits/stdc++.h>

using namespace std;

int n, p;
int cnt[4];
int dp[110][110][110][110];

void set_max(int &a, int b) {
	a = max(a, b);
}

void main2() {
	cin >> n >> p;
	memset(cnt, 0, sizeof cnt);
	for (int i = 0; i < n; i++) {
		int g;
		cin >> g;
		cnt[g%p]++;
	}
	memset(dp, 0, sizeof dp);
	for (int sum = 0; sum <= n; sum++) {
		for (int i = 0; i <= cnt[0]; i++)
			for (int j = 0; j <= cnt[1]; j++)
				for (int k = 0; k <= cnt[2]; k++) {
					int z = sum - i - j - k;
					if (z > cnt[3] || z < 0)
						continue;
					int fresh = ((i * 0 + j * 1 + k * 2 + z * 3) % p) == 0;
					if (i < cnt[0])	set_max(dp[i+1][j][k][z], dp[i][j][k][z] + fresh);
					if (j < cnt[1]) set_max(dp[i][j+1][k][z], dp[i][j][k][z] + fresh);
					if (k < cnt[2]) set_max(dp[i][j][k+1][z], dp[i][j][k][z] + fresh);
					if (z < cnt[3]) set_max(dp[i][j][k][z+1], dp[i][j][k][z] + fresh);
				}
	}
	cout << dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]] << endl;
}

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
