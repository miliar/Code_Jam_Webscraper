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
#include <cassert>

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

char tt[55][55];

int R, C;
int nShooters, nEmpty;

int id[55][55];

int covered[2600][2];

const int dx[] = { -1, 1, 0, 0 };
const int dy[] = { 0, 0, -1, 1 };

set<int> vis;
bool go(int r, int c, int dir, bool first) {
	if (r < 0 || c < 0 || r >= R || c >= C)
		return true;

	if (tt[r][c] == '#')
		return true;

	if (tt[r][c] == '.') {
		vis.insert(id[r][c]);
	}

	if (tt[r][c] == '-' && !first)
		return false;

	if (tt[r][c] == '/') {
		dir = 3 - dir;
	}
	if (tt[r][c] == '\\') {
		dir = (2 + dir) % 4;
	}

	go(r + dy[dir], c + dx[dir], dir, false);
	
}

int g[220][220];
int used[220];

void go(int v, int val, int n) {
	if (used[v] == -1) {
		used[v] = val;
		int rv = (!val ? v : n + v);
		FI if (g[rv][i])
			go(i, 0, n);
		FI if (g[rv][n+i])
			go(i, 1, n);
	}
	else {
		assert(used[v] == val);
	}

}

int solve() {
	GI2(R, C);
	FIR(R) scanf("%s", tt[i]);
	nShooters = nEmpty = 0;
	REP(r, R) REP(c, C) if (tt[r][c] == '|') tt[r][c] = '-';

	REP(r, R) REP(c, C)
		if (tt[r][c] == '-')
			id[r][c] = nShooters++;
		else if (tt[r][c] == '.')
			id[r][c] = nEmpty++;

	
	FIR(nEmpty) covered[i][0] = covered[i][1] = -1;

	memset(g, 0, sizeof g);
	REP(r, R) REP(c, C) if (tt[r][c] == '-') for (int hor = 0; hor <= 1; ++hor) {
		vis.clear();
		bool ok1 = go(r, c, 2 * hor, true);
		bool ok2 = go(r, c, 2 * hor+1, true);
		if (ok1 && ok2) {
			for (int ee : vis) {
				assert(covered[ee][hor] == -1);
				covered[ee][hor] = id[r][c];
			}
		}
		else {
			int sid = id[r][c];
			if (hor == 0) {
				g[sid][nShooters + sid] = 1;
			}
			else
				g[nShooters + sid][sid] = 1;
		}
	}

	
	FIR(nEmpty) {
		if (covered[i][0] == -1 && covered[i][1] == -1)
			return false;

		if (covered[i][0] == covered[i][1])
			continue;

		if (covered[i][0] == -1) {
			int sid = covered[i][1];
			g[sid][nShooters + sid] = 1;
		} else if (covered[i][1] == -1) {
			int sid = covered[i][0];
			g[nShooters + sid][sid] = 1;
		}
		else {
			int sid0 = covered[i][0];
			int sid1 = covered[i][1];

			g[nShooters + sid0][nShooters + sid1] = 1;
			g[sid1][sid0] = 1;
		}
	}

	int sz = nShooters * 2;
	REP(k, sz) REP(i, sz) REP(j, sz)
		g[i][j] |= g[i][k] && g[k][j];

	FIR(sz) if (g[i][nShooters+i] && g[nShooters+i][i])
		return false;

	memset(used, -1, sizeof used);
	FIR(nShooters) {
		if (used[i] == -1) {
			if (g[i][nShooters + i])
				go(i, 1, nShooters);
			else
				go(i, 0, nShooters);
		}
	}

	REP(r, R) REP(c, C) if (tt[r][c] == '-') {
		int sid = id[r][c];
		if (used[sid] == 1)
			tt[r][c] = '|';
	}

	return true;
	
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();
		
		printf("Case #%d: %s\n", tc, res ? "POSSIBLE" : "IMPOSSIBLE");
		if (res) {
			FIR(R)
				puts(tt[i]);
		}
		
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'C';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 1;
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
