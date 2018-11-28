#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (ll i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

ll r[100];
ll q[100][100];
ll c[100];

void solve()
{
	ll n, p;
	cin >> n >> p;
	FOR(i,n) cin >> r[i];
	FOR(i,n) FOR(j,p) {
		cin >> q[i][j];
	}
	FOR(i,n) sort(q[i], q[i] + p);
	FOR(i,n) q[i][p] = 5111999111999111999;
	NUL(c);
	ll completed = 0;
	for (ll m=1; m<=1000000; ++m) {
		while (true) {
			bool fail = false;
			FOR(i,n) {
				while (q[i][c[i]] * 10 < 9 * m * r[i]) ++c[i];
				if (c[i] >= p) {
					fail = true;
					break;
				}
				if (q[i][c[i]] * 10 > 11 * m * r[i]) {
					fail = true;
					break;
				}
			}
			if (fail) {
				break;
			}
			++completed;
			FOR(i,n) {
				++c[i];
			}
		}
	}
	cout << completed;
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
