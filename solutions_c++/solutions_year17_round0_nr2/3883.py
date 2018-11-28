#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>
 
using namespace std;
 
#define FOR(k,a,b) for(int k=(a); k < (b); k++)
#define FORE(k,a,b) for(int k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)
 
#define ALL(c) (c).begin(), (c).end()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define RANGE(lb, x, ub) ((lb) <= (x) && (x) < (ub))
 
#define dump(x) cerr << #x << ": " << (x) << endl;
 
typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
 
const int INF = 1000000000;
const double EPS = 1e-10;
const double PI = acos(-1.0);

bool subtidy(ll n, ll base) {
	int d = (n / base) % 10;
	int e = (n / (10 * base)) % 10;
	return e == 0 || e <= d;
}

bool istidy(ll n) {
	ll base = 1;
	while(n / base > 0) {
		if(!subtidy(n, base)) {
			return false;
		} else {
			base *= 10;
		}
	}
	return true;
}
 
int main(void) {
	int T; cin >> T;
	REP(tcase, T) {
		ll n; cin >> n;

		for(ll base = 1; !istidy(n) && (n / base > 0); base *= 10) {
			int d = (n / base) % 10;
			n -= (d + 1) * base;
			//cerr << base << " " << n << endl;
		}

		printf("Case #%d: %lld\n", tcase + 1, n);
	}

    return 0;
}
