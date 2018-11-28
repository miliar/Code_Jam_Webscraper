#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

char flip(char c) {
	return (c == '-' ? '+' : '-');
}

void flip(string &s, int k, int i) {
	forn(j, k) {
		s[i+j] = flip(s[i+j]);
	}
}

int solve(string s, int k) {
	int n = s.size();
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (s[i] == '-') {
			if (i+k > n) { return -1; }
			++ans;
			flip(s, k, i);
		}
	}
	return ans;
}

int main(void) {
	int t; cin >> t;
	forn(i, t) {
		string s; cin >> s;
		int k; cin >> k;
		int ans = solve(s, k);
		if (ans == -1) {
			cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (i+1) << ": " << ans << endl;
		}
	}
	return 0;
}
