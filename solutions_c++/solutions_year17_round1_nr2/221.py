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

int n;
int P;
int r[1010];

int temp[1010];
PI g[1010][1010];

int pos[1010];

PI lims(int t, int have) {
	int a = 10 * have / (11 * t);
	while (11 * t*a < 10 * have)   ++a;
	int b = 10 * have / (9 * t);
	return PI(a, b);
}

int solve() {
	GI2(n, P);
	FI GI(r[i]);

	VI u;

	FI{
		REP(p, P) GI(temp[p]);
		sort(temp, temp + P);
		REP(p, P) {
			g[i][p] = lims(r[i], temp[p]);
			u.push_back(g[i][p].first);
			u.push_back(g[i][p].second);
		}
	}
	sort(ALL(u));
	u.erase(unique(ALL(u)), u.end());


	int res = 0;
	FI pos[i] = 0;

	for (int k : u) {
		while (true)
		{
			FI{
				int&  p = pos[i];
				while (p < P && g[i][p].second < k) ++p;
			}

			int ok = true;
			FI{
				int  p = pos[i];
				if (p < P && g[i][p].first <= k) continue;
				ok = false;
			}

			if (ok) {
				++res;
				FI ++pos[i];
			}
			else
				break;

		}
		
	}

	return res;

}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();
		
		printf("Case #%d: %d\n", tc, res);
		
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
