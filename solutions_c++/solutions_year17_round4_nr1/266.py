#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)


#define N 101

int dp[5][N][N][N];
int vis[5][N][N][N];

int step;
int g[N];
int n, P;

int go(int sum, int c1, int c2, int c3) {
	int& res = dp[sum][c1][c2][c3];
	if (vis[sum][c1][c2][c3] == step)
		return res;
	vis[sum][c1][c2][c3] = step;

	res = 0;
	if (c1 + c2 + c3 == 1)
		return res;

	if (c1) {
		int nsum = (sum + 1) % P;
		res = max(res, (nsum == 0) + go(nsum, c1 - 1, c2, c3));
	}
	if (c2) {
		int nsum = (sum + 2) % P;
		res = max(res, (nsum == 0) + go(nsum, c1, c2-1, c3));
	}
	if (c3) {
		int nsum = (sum + 1) % P;
		res = max(res, (nsum == 0) + go(nsum, c1, c2, c3-1));
	}

	return res;
}

int solve() {
	GI2(n, P);
	FI GI(g[i]);

	int mods[4] = { 0, 0, 0, 0 };
	FI ++mods[g[i] % P];

	if (mods[0] == n)
		return n;

	int res = go(0, mods[1], mods[2], mods[3]);
	return 1+ res + mods[0];
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		::step = tc;
		int res = solve();
		
		printf("Case #%d: %d\n", tc, res);
		
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'A';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 0;
		bool LARGE = false;

		if (LARGE) {
			sprintf(in_file, "%c-large.in", TASK);
			sprintf(out_file, "%c-large.out", TASK);
		} else {
			sprintf(in_file, "%c-small-attempt%d.in", TASK,  ATTEMPT);
			sprintf(out_file, "%c-small-attempt%d.out", TASK,  ATTEMPT);
		}

		cerr << in_file <<  endl; freopen(in_file, "rt", stdin);
		cerr << out_file << endl; freopen(out_file, "w", stdout);
	}
}
