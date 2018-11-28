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

const int N = (int) 0, mod = (int) 0;

int main() {
	int tc;
	cin >> tc;
	for (int it = 1; it <= tc; ++it) {
		string s;
		int k, res = 0;
		cin >> s >> k;
		int n = (int) s.size();
		for (int j = 0; j < n - k + 1; ++j) {
			if (s[j] == '-') {
				++res;
				for (int i = j; i < j + k; ++i)
					if (s[i] == '-') {
						s[i] = '+';
					} else {
						s[i] = '-';
					}
			}
		}
		for (int j = 0; j < n; ++j)
			if (s[j] == '-') 
				res = -1;
		cout << "Case #" << it << ": ";
		if (res < 0) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << res << '\n';
		}
	}
}

















