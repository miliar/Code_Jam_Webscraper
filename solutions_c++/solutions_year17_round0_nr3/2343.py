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
const int N = (int) 1e7 + 6, mod = (int) 0;
int32_t main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		int n, k;
		cin >> n >> k;
		map<int, int> cnt;
		set<int, greater<int>> st;
		cnt[n]++;
		st.insert(n);
		while ((int) st.size()) {
			int x = *(st.begin());
			if (x == 0) {
				assert(0);
			}
			if (cnt[x] >= k) {
				--x;
				cout << (x >> 1) + (x & 1) << ' ' << (x >> 1);
				break;
			}
			int &c = cnt[x];
			st.erase(x);
			k -= c;
			--x;
			st.insert((x >> 1) + (x & 1));
			st.insert((x >> 1));
			cnt[x >> 1] += c;
			cnt[(x >> 1) + (x & 1)] += c;
		}
		cout << endl;
	}
}

















