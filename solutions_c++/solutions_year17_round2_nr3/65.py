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

LL inf = 1000000000000000LL;
const int N = 101;
int n, q;
int E[N], S[N];
LL d[N][N];
double res[N][N];
void solve() {
	cin >> n >> q;
	REP(i, n) {
		cin >> E[i] >> S[i];
	}
	REP(i, n) {
		REP(j, n) {
			cin >> d[i][j];
			if (i == j) {
				d[i][j] = 0;
			} else if (d[i][j] == -1) {
				d[i][j] = inf;
			}
		}
	}
	REP(k, n) {
		REP(i, n) {
			REP(j, n) {
				if (d[i][j] > d[i][k] + d[k][j]) {
					d[i][j] = d[i][k] + d[k][j];
				}
			}
		}
	}
	// printf("odl: \n");
	// REP(i, n) {
	// 	REP(j, n) printf("%lld ", d[i][j]);
	// 	printf("\n");
	// }
	REP(i, n) res[i][i] = 0;
	REP(i, n) REP(j, n) {
		if (d[i][j] <= 	E[i]) {
			res[i][j] = (double)d[i][j] / S[i];
		} else {
			res[i][j] = inf;
		}
	}
	// printf("res przed floyd: \n");
	// REP(i, n) {
	// 	REP(j, n) printf("%lf ", res[i][j]);
	// 	printf("\n");
	// }
	REP(k, n) REP(i, n) REP(j, n) if (res[i][j] > res[i][k] + res[k][j]) res[i][j] = res[i][k] + res[k][j];
	cout.precision(10);
	REP(i, q) {
		int a, b;
		cin >> a >> b;
		cout << res[a - 1][b - 1] << ' ';
	}
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		solve();
	}
}