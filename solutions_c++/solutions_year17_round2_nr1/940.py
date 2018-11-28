/*
 _    _    _______   _    _
| |  / /  |  _____| | |  / /
| | / /   | |       | | / /
| |/ /    | |_____  | |/ /
| |\ \    |  _____| | |\ \
| | \ \   | |       | | \ \
| |  \ \  | |_____  | |  \ \
|_|   \_\ |_______| |_|   \_\

*/
#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <cstring>
#include <string>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <assert.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef double ld;
typedef pair <int, int> PII;
typedef pair <ll, ll> PLL;

#define F first
#define S second
#define pb push_back
#define eb emplace_back
#define right(x) x << 1 | 1
#define left(x) x << 1
#define forn(x, a, b) for (int x = a; x <= b; ++x)
#define for1(x, a, b) for (int x = a; x >= b; --x)
#define mkp make_pair
#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define y1 kekekek

const long long ool = 1e18 + 9;
const int oo = 1e9 + 9, base = 1e9 + 7;
const double eps = 1e-7;
const int N = 2e3 + 6;

int n;
pair < ld, ld > a[N];

ld get(pair < ld, ld > a, pair < ld, ld > b) {
	if (a.S <= b.S) return -1.0;
	return (a.F * b.S - a.S * b.F) / (b.S - a.S);
}

int main() {
	ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);
	
	#ifdef KEK
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif

	int ts;
	cin >> ts;
	forn(test, 1, ts) {
		ld D;
		cin >> D >> n;
		forn(i, 1, n) {
			cin >> a[i].F >> a[i].S;
		}
		sort(a + 1, a + n + 1);
		a[n + 1].F = D;
		a[n + 1].S = 0;
		ld ans = 0;
		forn(i, 1, n + 1) {
			int mn = i + 1;
			forn(j, i + 2, n + 1) {
				if (get(a[i], a[mn]) == -1.0 || (get(a[i], a[j]) != -1.0 && get(a[i], a[mn]) - get(a[i], a[j]) > eps)) mn = j;
			}
			if (mn == n + 1) ans = (D - a[i].F) / a[i].S;
			i = mn - 1;
		}
		cout << fixed << setprecision(7) << "Case #" << test << ": " << D / ans << "\n";
	}

	return 0;
}
