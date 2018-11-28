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

string tidyest(const string &s, int i) {
	if (i == (int) s.size() - 1) {
		return string(1, s[s.size()-1]);
	} else {
		string r = tidyest(s, i+1);
		if (s[i] <= r[0]) {
			return s[i] + r;
		} else {
			return (char(s[i] - 1) + string(r.size(), '9'));
		}
	}
}

string solve(string s) {
	while (s[0] == '0') {
		s = s.substr(1);
	}
	string r = tidyest(s, 0);
	while (r[0] == '0') {
		r = r.substr(1);
	}
	return r;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		string s; cin >> s;
		string ans = solve(s);
		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
