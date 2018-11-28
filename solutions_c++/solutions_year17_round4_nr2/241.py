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


int q[1010];

VI tickets[1010];
int byp[1010];
int nSeats, nC, nSold;

int go(int t) {
	int sum = 0;
	int res = 0;
	FORE(p, 1, nSeats) {
		int h = tickets[p].size();
		if (h > t) {
			if (h + sum > t*p)
				return -1;

			res += h - t;
		}
		
		sum += h;
	}

	return res;
}

PI solve() {
	
	GI(nSeats); GI2(nC, nSold);
	int p, c;
	REP(i, 1010) tickets[i].clear();
	memset(byp, 0, sizeof byp);
	FIR(nSold) {
		GI2(p, c);
		tickets[p].push_back(c);
		++byp[c];
	}

	int res = 0;
	FORE(i, 0, nC) res = max(res, byp[i]);

	while (true) {
		int proms = go(res);
		if (proms >= 0)
			return PI(res, proms);
		++res;
	}

}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		PI res = solve();
		
		printf("Case #%d: %d %d\n", tc, res.first, res.second);
		
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'B';

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
