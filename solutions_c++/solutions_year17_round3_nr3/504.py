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
typedef long long li;

const int K = 1000;
const int N = 1450;
const int INF = 1e9;


void solve() {
	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++) {
		int n, k; double all;
		cin >> n >> k >> all;
		
		vector<double> p(n);
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}

		double l = 0.0;
		double r = 1.0;
		double mid = (l + r) / 2.0;
		
		for (int j = 0; j < 800; j++) {
			mid = (l + r) / 2.0;
			double need = 0.0;
			for (int i = 0; i < n; i++) {
				if (p[i] >= mid) continue;
				need += mid - p[i];
			}
			if (need <= all)
				l = mid;
			else
				r = mid;
		}

		double ans = 1.0;
		for (int i = 0; i < n; i++) {
			if (p[i] < mid) {
				double can = min(all, mid - p[i]);
				p[i] += can;
				all -= can;
			}
			ans *= p[i];
		}
		cout.precision(8);
		cout << "Case #" << q + 1 << ": " << fixed << ans << endl;
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