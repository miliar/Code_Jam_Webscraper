/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>

#define ll long long
#define ld double
#define pii pair <int, int>
#define pll pair <ll, ll>
#define mp make_pair

using namespace std;

int cnt[4];

int dp[101][101][101][4][4];

int go(int a, int b, int c, int o, int p) {
	if (dp[a][b][c][o][p] != -1) {
		return dp[a][b][c][o][p];
	}

	if (a == 0 && b == 0 && c == 0) {
		return dp[a][b][c][o][p] = 0;
	}

	int v[3] = {a, b, c};

	int ans = 0;

	for (int i = 1; i <= p - 1; i++) {
		int pos = i - 1;
		if (v[pos] != 0) {
			ans = max(ans, go(a - (pos == 0), b - (pos == 1), c - (pos == 2), (o + i) % p, p) + (o == 0));
		}
	}

	return dp[a][b][c][o][p] = ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	memset(dp, -1, sizeof dp);

	for (int itt = 1; itt <= t; itt++) {
		printf("Case #%d: ", itt);

		int n, p;

		cin >> n >> p;

		memset(cnt, 0, sizeof cnt);

		for (int i = 0; i < n; i++) {
			int x;

			scanf("%d", &x);

			cnt[x % p]++;
		}

		int ans = cnt[0] + go(cnt[1], cnt[2], cnt[3], 0, p);

		printf("%d\n", ans);
	}

	return 0;
}
