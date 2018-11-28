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

const int N = 101;
int F[N][N];
int G[N][N][N];
int resz[4];

void solve() {
	int n, p;
	cin >> n >> p;
	REP(i, p) resz[i] = 0;
	int sum = 0;
	REP(i, n) {
		int x;
		cin >> x;
		if (x % p == 0) {
			++sum;
		} else {
			++resz[x % p];
		}
	}
	if (p == 2) {
		cout << sum + (resz[1] + 1) / 2 << endl;
	} else if (p == 3) {
		cout << sum + F[resz[1]][resz[2]] << endl;
	} else {
		cout << sum + G[resz[1]][resz[2]][resz[3]] << endl;
	}
}

int main() {
	REP(i, N) REP(j, N) {
		if (i == 0 && j == 0) continue;
		// i x 1, j x 2
		int ile = 1;
		if (i > 0 && j > 0) {
			ile = F[i-1][j-1] + 1;
		}
		if (i >= 3) {
			ile = max(ile, F[i-3][j] + 1);
		}
		if (j >= 3) {
			ile = max(ile, F[i][j -3] + 1);
		}
		F[i][j] = ile;
	}
	REP(i, N) REP(j, N) REP(k, N) {
		if (i+j+k == 0) {
			continue;
		}
		int ile = 1;
		if (i >= 4) {
			ile = G[i-4][j][k] + 1;
		}
		if (j >= 2) {
			ile = max(ile, G[i][j - 2][k] + 1);
		}
		if (k >= 4) {
			ile = max(ile, G[i][j][k - 4] + 1);	
		}
		if (i > 0 && k > 0) {
			ile = max(ile, G[i - 1][j][ k - 1] + 1);
		}
		if (i >= 2 && j) {
			ile = max(ile, G[i - 2][j - 1][k] + 1);
		}
		if (j && k >= 2) {
			ile = max(ile, G[i][j - 1][k - 2] + 1);
		}
		G[i][j][k] = ile;
	}
	int t;
	cin >> t;
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		solve();
	}
}