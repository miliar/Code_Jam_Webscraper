#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

using namespace std;

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

template<typename T> inline void swap(pair<T, T> &p) { swap(p.first , p.second ); }

#define all(v) v.begin(),v.end()

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) { if (i) os << ' '; os << v[i]; } os << endl; return os; }
template <typename T1, typename T2> ostream& operator << (ostream& os, const vector<pair<T1, T2>> &v) { for (int i = 0 ; i < v.size() ; i++) { os << v[i] << endl; } return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

void assert2(bool x) {
	if (!x) exit(0);
}

int solve() {
	next(int, n);
	next(int, p);

	auto sizes = readVector<int>(n);
	
	vector<int> rems(4);
	for (auto &x : sizes) rems[x % p]++;

	int ans = rems[0];
	rems[0] = 0;
	if (p == 2) {
		ans += rems[p / 2] / 2;
		rems[p / 2] &= 1;
	} else if (p == 3) {
		int x = min(rems[1], rems[2]);
		ans += x;
		rems[1] -= x;
		rems[2] -= x;

		ans += rems[1] / 3;
		rems[1] %= 3;
		ans += rems[2] / 3;
		rems[2] %= 3;
	} else {
		assert2(p == 4);

		ans += rems[p / 2] / 2;
		rems[p / 2] &= 1;

		int x = min(rems[1], rems[3]);
		ans += x;
		rems[1] -= x;
		rems[3] -= x;

		if (rems[2]) {
			if (rems[1] > 1) {
				rems[1] -= 2;
				rems[2] --;
				ans++;
			}
			if (rems[3] > 1) {
				rems[3] -= 2;
				rems[2] --;
				ans++;
			}

		}
		if (rems[2] == 0) {
			ans += rems[1] / 4;
			rems[1] %= 4;
			ans += rems[3] / 4;
			rems[3] %= 4;
		}
	}
	if (accumulate(all(rems), 0) > 0) ans++;
	return ans;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);
	
	next(int, n);
	FOR (i, 0, n) {
		cout << "Case #" << (i + 1) << ": ";
		auto res = solve();
		// if (res == -1) cout << "IMPOSSIBLE" << endl;
		// else 
			cout << res << endl;
		// cout << endl;
	}

	cerr << "Done" << endl;
}