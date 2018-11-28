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
 
int main(void) {
	int T; cin >> T;
	REP (tcase, T) {
		int n, k; cin >> n >> k;
		priority_queue<int> q;
		q.push(n);

		int l, r;
		for (int i = 0; i < k; i++) {
			int m = q.top(); q.pop();
			int a = (m - 1) / 2;
			int b = m - 1 - a;
			l = min(a, b); r = max(a, b);
			if (a > 0) q.push(a);
			if (b > 0) q.push(b);
		}

		printf("Case #%d: %d %d\n", tcase + 1, r, l);
	}

    return 0;
}
