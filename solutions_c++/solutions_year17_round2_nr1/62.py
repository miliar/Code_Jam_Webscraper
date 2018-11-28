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

double d;
int n;

void solve() {
	cin >> d >> n;
	double maxCzas = -1;
	REP(i, n) {
		double k, s;
		cin >> k >> s;
		double curCzas = (d - k) / s;
		if (maxCzas == -1 || curCzas > maxCzas) {
			maxCzas = curCzas;
		}

	}
	cout.precision(10);
	double res = d / maxCzas;
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		solve();
	}
}