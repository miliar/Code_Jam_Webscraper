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
double e[MAXN], s[MAXN];
double dist[MAXN][MAXN];
void floyd(int n) {
	for (int k = 1; k <= n; ++k) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}
}
double dp[MAXN][MAXN];
double gao(int n, int u, int v) {
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			dp[i][j] = 1e12;
		}
	}
	dp[u][u] = 0;
	queue<pair<int, int> > q;
	q.push(make_pair(u, u));
	while (!q.empty()) {
		pair<int, int> head = q.front();
		q.pop();
		for (int i = 1; i <= n; ++i) {
			if (dist[head.second][head.first] + dist[head.first][i]
					<= e[head.second]) {
				double tmp = dp[head.first][head.second]
						+ dist[head.first][i] / s[head.second];
				if (tmp < dp[i][head.second]) {
					dp[i][head.second] = tmp;
					q.push(make_pair(i, head.second));
				}
			}
			if (dist[head.first][i] <= e[head.first]) {
				double tmp = dp[head.first][head.second]
						+ dist[head.first][i] / s[head.first];
				if (tmp < dp[i][head.first]) {
					dp[i][head.first] = tmp;
					q.push(make_pair(i, head.first));
				}
			}
		}
	}

	double ans = 1e12;
	for (int i = 1; i <= n; ++i) {
		ans = min(ans, dp[v][i]);
	}
	return ans;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n, q;
		cin >> n >> q;
		for (int i = 1; i <= n; ++i) {
			cin >> e[i] >> s[i];
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				cin >> dist[i][j];
				if (dist[i][j] < 0) {
					dist[i][j] = 1e12;
				}
			}
		}
		floyd(n);
		printf("Case #%d:", t);
		while (q--) {
			int u, v;
			cin >> u >> v;
			printf(" %.8lf", gao(n, u, v));
		}
		puts("");
	}
	return 0;
}
