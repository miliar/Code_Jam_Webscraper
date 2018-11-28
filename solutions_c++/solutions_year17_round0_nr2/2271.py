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
#define int long long
const int N = (int) 20, mod = (int) 0;
char res[N];
int32_t main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt <<": ";
		string s;
		cin >> s;
		int n = (int) s.size();
		for (int dig = 0; dig < n; ++dig) {
			for (int use = 9; use >= 0; --use) {
				int ok = 1;
				for (int j = dig; j < n; ++j)
					res[j] = '0' + use;
				for (int j = 0; j < n; ++j) 
					if (res[j] != s[j]) {
						if (res[j] > s[j]) {
							ok = 0;
						}
						break;
					}
				if (ok) break;
			}
		}
		int pt = 0;
		while (res[pt] == '0') ++pt;
		for (int j = pt; j < n; ++j)
			cout << res[j];
		cout << '\n';
	}
}

















