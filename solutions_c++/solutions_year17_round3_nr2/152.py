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
const ll maxn = (ll)3e3 + 10;
const ll maxlog = (ll)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e9 + 7;
const ld eps = 1e-7;
const int maxm = 24 * 60;
const int maxk = 720;

int n, m, k, t, x, y, a[maxn];
int dp[maxn][maxn][3][3];
int it;

int solve(int pos, int time1, int pr, int st) {
	if (pos == 1 && time1 == 0) {
		pos = pos;
	}
	if (pos == maxm) {
		if (time1 == maxk) {
			if (st == pr) {
				return 0;
			}
			else {
				return 1;
			}
		}
		else {
			return -1;
		}
	}
	if (dp[pos][time1][pr][st] != -2) {
		return dp[pos][time1][pr][st];
	}
	it++;
	int tans = inf;
	int tmp = 0;

	if (a[pos]) {
		if (a[pos] == 1) {
			if (time1 == maxk) {
				tans = -1;
				dp[pos][time1][pr][st] = tans;
				return -1;
			}
			if (pos == 0) {
				st = 1;
			}
			tmp = solve(pos + 1, time1 + 1, 1, st);
			if (tmp != -1) {
				tmp += (pr == 1 || pr == 0 ? 0 : 1);
				tans = min(tans, tmp);
			}
		}
		else {
			if (pos - time1 == maxk) {
				tans = -1;
				dp[pos][time1][pr][st] = tans;
				return -1;
			}
			if (pos == 0) {
				st = 2;
			}
			tmp = solve(pos + 1, time1, 2, st);
			if (tmp != -1) {
				tmp += (pr == 1 ? 1 : 0);
				tans = min(tans, tmp);
			}
		}
	}
	else {
		if (time1 != maxk) {
			if (pos == 0) {
				st = 1;
			}
			tmp = solve(pos + 1, time1 + 1, 1, st);
			if (tmp != -1) {
				tmp += (pr == 1 || pr == 0 ? 0 : 1);
				tans = min(tans, tmp);
			}
		}
		if (pos - time1 != maxk) {
			if (pos == 0) {
				st = 2;
			}
			tmp = solve(pos + 1, time1, 2, st);
			if (tmp != -1) {
				tmp += (pr == 1 ? 1 : 0);
				tans = min(tans, tmp);
			}
		}
	}
	if (tans == inf) {
		tans = -1;
	}
	dp[pos][time1][pr][st] = tans;
	return tans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> m;
		memset(a, 0, sizeof a);
		for (int i = 0; i < n; i++) {
			cin >> x >> y;
			for (int j = x; j < y; j++) {
				a[j] = 1;
			}
		}
		for (int i = 0; i < m; i++) {
			cin >> x >> y;
			for (int j = x; j < y; j++) {
				a[j] = 2;
			}
		}
		for (int i = 0; i < maxn; i++) {
			for (int j = 0; j < maxn; j++) {
				for (int z = 0; z < 3; z++) {
					for (int w = 0; w < 3; w++) {
						dp[i][j][z][w] = -2;
					}
				}
			}
		}
		it = 0;
		printf("Case #%d: %d\n", ii + 1, solve(0, 0, 0, 0));
		cerr << it << endl;
	}
	return 0;
}