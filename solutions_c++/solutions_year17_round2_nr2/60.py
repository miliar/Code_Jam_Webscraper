#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=(b); x<=(e); ++x)
#define FORD(x, b, e) for(int x=((int)(b))-1; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) ((int)((x).size()))
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FOREACH(it, (x)) cerr <<*it <<", "; cout <<endl; }}
typedef short int sint;

int pom[6], oryg[6];
bool isNajw(int a, int b, int c) {
	return a >= b && a >= c;
}

char getcharek(int kt) {
	if (kt == 0) return 'R';
	if (kt == 1) return 'O';
	if (kt == 2) return 'Y';
	if (kt == 3) return 'G';
	if (kt == 4) return 'B';
	return 'V';
}

int getSec(int kt) {
	if (kt == 0) return 3;
	if (kt == 2) return 5;
	return 1;
}

void solve() {
	int n;
	int r, o, y, g, b, v;
	cin >> n ;
	REP(i, 6) cin >> pom[i];
	REP(i, 6) oryg[i] = pom[i];
	// r y b
	int kt = 0;
	pom[4] -= pom[1];
	pom[0] -= pom[3];
	pom[2] -= pom[5];
	// cout << pom[0] << ' ' << pom[2] << ' ' << pom[4] << endl;
	int pom1 = 2, pom2 = 4;
	if (isNajw(pom[2], pom[0], pom[4])) {
		kt = 2;
		pom1 = 0, pom2 = 4;
	} else if (isNajw(pom[4], pom[0], pom[2])) {
		kt = 4;
		pom1 = 0, pom2 = 2;
	}
	if (pom[0] < 0 || pom[2] < 0 || pom[4] < 0 || (2 * pom[kt] > pom[0] + pom[2] + pom[4])) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	string result;
	int ost = -1;
	int ile = pom[0] + pom[2] + pom[4];
	if (ile == 0) {
		int ile = 0;
		for (int i = 0; i < 6; i+=2) {
			if (oryg[i] > 0) {
				++ile;
				kt = i;
			}
		}
		if (ile > 1) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		int drug = getSec(kt);
		REP(i, oryg[kt]) {
			cout << getcharek(kt) << getcharek(drug);
		}
		cout << endl;
		return;
	}
	REP(i, ile) {
		if (ost != kt && pom[kt] > 0) {
			ost = kt;
			--pom[kt];
			result = result + getcharek(kt);
		} else {
			// pom1 lub pom2
			if (ost != pom1 && pom[pom1] > pom[pom2]) {
				ost = pom1;
				--pom[pom1];
				result = result + getcharek(pom1);
			} else {
				ost = pom2;
				--pom[pom2];
				result = result + getcharek(pom2);
			}
		}
		// ost mamy
		int drug = getSec(ost);
		while (pom[drug] > 0) {
			result = result + getcharek(drug) + getcharek(ost);
			--pom[drug];
		}
	}
	int zost = pom[1] + pom[3] + pom[5];
	if (zost > 0) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << result << endl;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		solve();
	}
}