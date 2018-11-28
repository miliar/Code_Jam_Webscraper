#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);

#define REP(i,n)	for(int i=0;i<(int)n;++i)
#define ALL(c)		(c).begin(),(c).end()
#define CLEAR(v)	memset(v,0,sizeof(v))
#define MP(a,b)		make_pair((a),(b))
#define ABS(a)		((a)>0?(a):-(a))
#define FOR(i,s,n)	for(int i=s;i<(int)n;++i)

#define IMPOSSIBLE "IMPOSSIBLE"

int solve_s(string s, int k, int i, int cnt) {
	if (i > s.length() - k) {
		REP(j, s.length()) if (s[j] != '+') return s.length() + 1;
		return cnt;
	}
	int res1 = solve_s(s, k, i + 1, cnt);
	REP(j, k) s[i + j] = (s[i + j] == '+' ? '-' : '+');
	int res2 = solve_s(s, k, i + 1, cnt + 1);
	return min(res1, res2);
}

void solve() {
	string s;
	int k;
	cin >> s >> k;
	int res = solve_s(s, k, 0, 0);
	if (res > s.length()) cout << IMPOSSIBLE << endl;
	else cout << res << endl;
}

int main(int argc, char **argv) {
	int n;
	cin >> n;
	REP(i, n) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
	return 0;
}
