//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <queue>
using namespace std;
#define MAXN 110
#define oo 1e9
#define MOD 1000000007
#define EPS 1e-8
typedef long long LL;
int arr[MAXN];
int dp[MAXN][MAXN][MAXN][4];
map<int, int> counter;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		counter.clear();
		int ans = 0;
		int n, p;
		cin >> n >> p;
		for (int i = 0; i < n; ++i) {
			cin >> arr[i];
			arr[i] %= p;
			counter[arr[i]]++;
		}
		memset(dp, -1, sizeof(dp));
		dp[0][0][0][0] = 0;
		for (int i = 0; i <= counter[1]; ++i) {
			for (int j = 0; j <= counter[2]; ++j) {
				for (int k = 0; k <= counter[3]; ++k) {
					for (int l = 0; l < p; ++l) {
						if (dp[i][j][k][l] == -1) {
							continue;
						}
						//printf("%d,%d,%d,%d %d\n", i, j, k, l, dp[i][j][k][l]);
						int add = l == 0 ? 1 : 0;
						if (i < counter[1])
							dp[i + 1][j][k][(l + 1) % p] = max(
									dp[i + 1][j][k][(l + 1) % p],
									dp[i][j][k][l] + add);
						if (j < counter[2])
							dp[i][j + 1][k][(l + 2) % p] = max(
									dp[i][j + 1][k][(l + 2) % p],
									dp[i][j][k][l] + add);
						if (k < counter[3])
							dp[i][j][k + 1][(l + 3) % p] = max(
									dp[i][j][k + 1][(l + 3) % p],
									dp[i][j][k][l] + add);
						ans = max(ans, dp[i][j][k][l]);
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, ans + counter[0]);
	}
	return 0;
}
