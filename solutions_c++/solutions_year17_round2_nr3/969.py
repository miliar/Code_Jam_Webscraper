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
const double eps = 1e-8;
const int N = 111;

pair < ld, ld > a[N];
ld d[N][N], dist[N][N];

int main() {
	ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);
	
	#ifdef KEK
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif

	int ts;
	cin >> ts;
	forn(test, 1, ts) {
		int n, q;
		cin >> n >> q;
		forn(i, 1, n) {
			cin >> a[i].F >> a[i].S;			
		}

		forn(i, 1, n) {
			forn(j, 1, n) {
				cin >> d[i][j];
				if (d[i][j] == -1) d[i][j] = 1e18;
				dist[i][j] = d[i][j];
				if (i == j) d[i][j] = dist[i][j] = 0;
				if (d[i][j] != 1e18 && d[i][j] <= a[i].F) d[i][j] /= a[i].S;
				else d[i][j] = 1e18;
			}
		}

		forn(k, 1, n) {
			forn(i, 1, n) {
				forn(j, 1, n) {
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}

		forn(k, 1, n) {
			forn(l, 1, n) {
				if (k == l) continue;
				if (dist[k][l] > a[k].F) continue;
				ld w = dist[k][l] / a[k].S;
				forn(i, 1, n) {
					forn(j, 1, n) {
						if (d[i][j] - (d[i][k] + w + d[l][j]) > eps) d[i][j] = d[i][k] + w + d[l][j];
					}
				}
			}
		}


		cout << "Case #" << test << ":";
		forn(i, 1, q) {
			int v, u;
			cin >> v >> u;
			cout << fixed << setprecision(8) << " " << d[v][u];
		}
		cout << "\n";
	}

	return 0;
}
