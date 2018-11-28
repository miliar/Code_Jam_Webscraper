/*
 * GCJ 2017 round 2
 * Task: A. Fresh Chocolate
 */
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const int INF = 999666111;
const int MAXN = 1001;

int dyn[101][101][101][101][4];
int n, p;
int g[10];

int f(int r0, int r1, int r2, int r3, int remainder)
{
	int ng = r0 + r1 + r2 + r3;
	if (!ng) return 0;
	
	int& dp = dyn[r0][r1][r2][r3][remainder];
	
	if (dp != -1) return dp;
	dp = 0;
	if (r0) dp = max(dp, f(r0 - 1, r1, r2, r3, remainder));
	if (r1) dp = max(dp, f(r0, r1 - 1, r2, r3, (remainder-1+p) % p));
	if (r2) dp = max(dp, f(r0, r1, r2 - 1, r3, (remainder-2+p) % p));
	if (r3) dp = max(dp, f(r0, r1, r2, r3 - 1, (remainder-3+p) % p));
	if (remainder == 0) dp++;
	return dp;
}

int solve()
{
	memset(dyn, 0xff, sizeof(dyn));
	memset(g, 0, sizeof(g));
	
	scanf("%d%d", &n, &p);
	FOR(i, n) {
		int x;
		scanf("%d", &x);
		g[x % p]++;
	}
	return f(g[0], g[1], g[2], g[3], 0);
}

int main(void)
{
//	//freopen("/home/vesko/gcj/a.in", "rt", stdin);
	
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %d\n", tc, solve());
	
	}
	
	return 0;
}
