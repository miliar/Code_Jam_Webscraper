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

struct space {
	LL size, count;
};

pair<LL, LL> split_space(LL n) {
	assert2(n > 0);
	n--;
	return { n / 2 , n - n/2};
}

void add_space(deque<space> &spaces, LL sz, LL cnt) {
	if (spaces.size() && spaces.back().size == sz) spaces.back().count += cnt;
	else spaces.push_back( { sz , cnt });
}

pair<LL, LL> solve() {
	next(LL, n);
	next(LL, k);

	deque<space> spaces = { { n , 1 } };
	k--;

	while (k > 0) {
		auto num = min(k, spaces.front().count);
		// cout << "splitting " << num << " out of " << spaces.front().count << " of size " << spaces.front().size << endl;
		auto splits = split_space(spaces.front().size);
		spaces.front().count -= num;
		if (spaces.front().count == 0) spaces.pop_front();
		k -= num;

		add_space(spaces, splits.second, num);
		add_space(spaces, splits.first, num);
	}

	return { split_space(spaces.front().size).second , 
		     split_space(spaces.front().size).first };
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);
	
	next(int, n);
	FOR (i, 0, n) {
		auto res = solve();
		cout << "Case #" << (i + 1) << ": ";
		// if (res == -1) cout << "IMPOSSIBLE" << endl;
		// else 
			cout << res << endl;
	}

	cerr << "Done" << endl;
}