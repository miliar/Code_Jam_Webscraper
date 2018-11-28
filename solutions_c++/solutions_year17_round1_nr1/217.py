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

int R, C;

char a[100][100];
int emp[100];

void solve() {
	GI2(R, C);
	FIR(R) scanf("%s", a[i]);
	REP(r, R) emp[r] = true;

	REP(r, R) {
		bool found = 0;
		REP(c, C) if (a[r][c] != '?') {
			emp[r] = false;
			for (int cc = c - 1; cc >= 0; --cc) if (a[r][cc] == '?') a[r][cc] = a[r][c]; else break;
			for (int cc = c + 1; cc < C; ++cc) if (a[r][cc] == '?') a[r][cc] = a[r][c]; else break;
		}
		if (emp[r] && r && !emp[r-1]) {
			REP(c, C) a[r][c] = a[r - 1][c];
			emp[r] = false;
		}
	}

	FORD(r, R - 1, 0) if (emp[r]) {
		REP(c, C) a[r][c] = a[r + 1][c];
	}

	REP(r, R) {
		puts(a[r]);
	}
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		
		
		printf("Case #%d:\n", tc);
		solve();
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
		bool LARGE = true;

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
