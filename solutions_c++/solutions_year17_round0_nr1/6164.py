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

const int N = 1010;
int wys[N];
string inp;
int k;
int n;

void solve() {
	cin >> inp >> k;
	n = SIZE(inp);
	int cur = 0;
	int wyn = 0;
	REP(i, n) wys[i] = 0;
	REP(i, n) {
		int coMam = inp[i] == '-';
		cur += wys[i];
		if ((coMam + cur) & 1) {
			if (i < n - k + 1) {
				++wyn;
				++cur;
				--wys[i + k];
			} else {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
	}
	cout << wyn << endl;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		solve();
	}
}