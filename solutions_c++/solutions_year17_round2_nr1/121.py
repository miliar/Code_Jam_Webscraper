// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;
#define double long double
const int N = (int) 1e5 + 5, mod = (int) 0;
int pos[N], speed[N];
int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		int n;
		double dreach;
		cin >> dreach >> n;
		for (int j = 0; j < n; ++j)
			cin >> pos[j] >> speed[j];
		double bl = 0, br = 1e19;
		for (int k = 0; k < 200; ++k) {
			double bm = (bl + br) / 2;
			int ok = 1;
			for (int j = 0; j < n; ++j) {
				if (speed[j] < bm) {
					double treach = (pos[j] / (double) (bm - speed[j]));
					double reach = treach * bm;
					if (reach <= dreach) {
						ok = 0;
					}
				}
			}
			if (ok) {
				bl = bm;
			} else {
				br = bm;
			}
		}
		cout << setprecision(8) << fixed << bl << endl;
	}
}

















