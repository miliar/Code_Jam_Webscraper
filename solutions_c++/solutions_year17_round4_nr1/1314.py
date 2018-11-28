#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

const int N = 105;
int dp[4][N][N][N];

const int inf = 1e9;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++) {
		int n;
		cin >> n;
		int p;
		cin >> p;
		vector<int> v;
		int zeroes = 0;
		int u[3] = { 0, 0, 0 };
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			x %= p;
			if (x == 0) {
				zeroes++;
			}
			else {
				v.push_back(x);
				u[x - 1]++;
			}
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					for (int t = 0; t < N; t++) {
						dp[i][j][k][t] = -inf;
					}
				}
			}
		}
		dp[0][u[0]][u[1]][u[2]] = zeroes;
		for (int a = N - 3; a >= 0; a--) {
			for (int b = N - 3; b >= 0; b--) {
				for (int c = N - 3; c >= 0; c--) {
					for (int rem = 0; rem < p; rem++) {
						if (dp[(rem + 1) % p][a + 1][b][c] != -inf)
							dp[rem][a][b][c] = max(dp[rem][a][b][c], dp[(rem + 1) % p][a + 1][b][c] + ((rem + 1) % p == 0));
						if (dp[(rem + 2) % p][a][b + 1][c] != -inf)
							dp[rem][a][b][c] = max(dp[rem][a][b][c], dp[(rem + 2) % p][a][b + 1][c] + ((rem + 2) % p == 0));
						if (dp[(rem + 3) % p][a][b][c + 1] != -inf)
							dp[rem][a][b][c] = max(dp[rem][a][b][c], dp[(rem + 3) % p][a][b][c + 1] + ((rem + 3) % p == 0));
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < p; i++) {
			ans = max(ans, dp[i][0][0][0]);
		}
		printf("Case #%d: %d\n", q + 1, ans);
	}

	return 0;
}