#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<iomanip>
#include <cassert>
#include<algorithm>
#include <map>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include <queue>
#include <string.h>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())
#define mp make_pair
#define X first;
#define Y second;
typedef long long li;

const int K = 1000;
const int N = 2450;
const int INF = 1e9;

const long double PI = 3.1415926535897932384626433832795;
li z[N][N], mxz[N][N];

#define X first
#define Y second

const li INF64 = 1e17;

void solve() {
	cout.precision(6);
	int test;
	cin >> test;
	for (int q = 0; q < test; q++) {
		int n, k;
		cin >> n >> k;
		vector < pair < li, li >> a(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}
		memset(z, 0, sizeof z);
		memset(mxz, 0, sizeof mxz);
		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());

		for (int r = 1; r <= k; r++) {
			if (r == 1)
				z[n - 1][r] = a[n - 1].X * a[n - 1].X + a[n - 1].X * a[n - 1].Y * 2;
			else
				z[n - 1][r] = -INF64;

			for (int idx = n - 2; idx >= 0; idx--) {
				if (r > 1)
					z[idx][r] = mxz[idx + 1][r - 1] + a[idx].X * a[idx].X + 2 * a[idx].X * a[idx].Y;

				else
					z[idx][r] = max(a[idx].X * a[idx].X + a[idx].X * a[idx].Y * 2, z[idx + 1][r]);
			}

			mxz[n - 1][r] = z[n - 1][r] - a[n - 1].X * a[n - 1].X;
			for (int idx = n - 2; idx >= 0; idx--) {
				mxz[idx][r] = max(z[idx][r] - a[idx].X * a[idx].X, mxz[idx + 1][r]);
			}
		}

		li ans = 0;
		for (int i = 0; i < n; i++) {
			ans = max(ans, z[i][k]);
		}
		cout << "Case #" << q + 1 << ": " << fixed << ans * PI << endl;
	}
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin.tie(0);
	cout.sync_with_stdio(false);
	
	solve();
	return 0;
}