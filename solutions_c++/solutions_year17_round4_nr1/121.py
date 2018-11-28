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

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

int n, p;
int r[4];

void solve()
{
	cin >> n >> p;
	FOR(i, p) r[i] = 0;
	FOR(i, n) {
		int a;
		cin >> a;
		++r[a % p];
	}
	int rem = 0;
	int good = 0;
	//FOR(i,p) cout << "x " << r[i] << endl;
	FOR(i, n) {
		//cout << "GROUP " << i << " REM " << rem << endl;
		if (rem == 0) ++good;
		int desire = (p - rem) % p;
		if (r[desire] > 0) {
			--r[desire];
			rem = 0;
		} else {
			bool found = false;

			FOR(j,p) {
				if (r[j] > 0 && r[(p - ((rem + j) % p)) % p] > 0) {
					--r[j];
					rem = (rem + j) % p;
					found = true;
					break;
				}
			}

			if (!found) {
				FOR(j,p) {
					if (r[j] > 0) {
						--r[j];
						rem = (rem + j) % p;
						break;
					}
				}
			}
		}
	}
	cout << good;
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
