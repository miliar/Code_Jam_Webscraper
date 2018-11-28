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
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>            
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const int maxn = (int)2e2 + 11;
const ll maxlog = (ll)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e18 + 7;
const ld eps = 1e-7;

int t, n, p, a[4], x;
int dp[101][101][101][101];

queue<pair<pair<int, int>, pair<int, int> > > q;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> p;
		memset(a, 0, sizeof a);
		for (int i = 0; i < n; i++) {
			cin >> x;
			a[x % p]++;
		}
		for (int i = 0; i <= a[0]; i++) {
			for (int j = 0; j <= a[1]; j++) {
				for (int z = 0; z <= a[2]; z++) {
					for (int u = 0; u <= a[3]; u++) {
						dp[i][j][z][u] = 0;
					}
				}
			}
		}
		if (a[0]) {
			dp[a[0] - 1][a[1]][a[2]][a[3]] = 1;
			q.push(mp(mp(a[0] - 1, a[1]), mp(a[2], a[3])));
		}
		if (a[1]) {
			dp[a[0]][a[1] - 1][a[2]][a[3]] = 1;
			q.push(mp(mp(a[0], a[1] - 1), mp(a[2], a[3])));
		}
		if (a[2]) {
			dp[a[0]][a[1]][a[2] - 1][a[3]] = 1;
			q.push(mp(mp(a[0], a[1]), mp(a[2] - 1, a[3])));
		}
		if (a[3]) {
			dp[a[0]][a[1]][a[2]][a[3] - 1] = 1;
			q.push(mp(mp(a[0], a[1]), mp(a[2], a[3] - 1)));
		}
		int ans = 0;
		while (!q.empty()) {
			int x = q.front().first.first;
			int y = q.front().first.second;
			int z = q.front().second.first;
			int u = q.front().second.second;
			q.pop();
			ans = max(ans, dp[x][y][z][u]);
			int cur = a[1] - y;
			cur += (a[2] - z) * 2;
			cur += (a[3] - u) * 3;
			cur %= p;
			if (x) {
				int tp = (cur == 0 ? 1 : 0);
				if (dp[x - 1][y][z][u] < dp[x][y][z][u] + tp) {
					dp[x - 1][y][z][u] = dp[x][y][z][u] + tp;
					q.push(mp(mp(x - 1, y), mp(z, u)));
				}
			}
			if (y) {
				if (dp[x][y - 1][z][u] < dp[x][y][z][u] + (cur == 0 ? 1 : 0)) {
					dp[x][y - 1][z][u] = dp[x][y][z][u] + (cur == 0 ? 1 : 0);
					q.push(mp(mp(x, y - 1), mp(z, u)));
				}
			}
			if (z) {
				if (dp[x][y][z - 1][u] < dp[x][y][z][u] + (cur == 0 ? 1 : 0)) {
					dp[x][y][z - 1][u] = dp[x][y][z][u] + (cur == 0 ? 1 : 0);
					q.push(mp(mp(x, y), mp(z - 1, u)));
				}
			}
			if (u) {
				if (dp[x][y][z][u - 1] < dp[x][y][z][u] + (cur == 0 ? 1 : 0)) {
					dp[x][y][z][u - 1] = dp[x][y][z][u] + (cur == 0 ? 1 : 0);
					q.push(mp(mp(x, y), mp(z, u - 1)));
				}
			}
		}
		printf("Case #%d: %d\n", ii + 1, ans);
	}
	return 0;
}