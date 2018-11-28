#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>
#include <stack>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define fst first
#define snd second

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef long double ld;

template<class T>
bool chmin(T& x, const T& y) {
	if (y < x) {
		x = y;
		return true;
	}
	return false;
}

template<class T>
bool chmax(T& x, const T& y) {
	if (x < y) {
		x = y;
		return true;
	}
	return false;
}

template<class T, class P>
ostream& operator <<(ostream& os, const pair<T, P>& p) {
	return os << "(" << p.first << ", " << p.second << ")";
}

template<class T>
ostream& operator <<(ostream& os, const vector<T>& v) {
	os << "[";
	bool was = false;
	for (const T& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T>
ostream& operator <<(ostream& os, const set<T>& v) {
	os << "[";
	bool was = false;
	for (const T& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T, class P>
ostream& operator <<(ostream& os, const map<T, P>& v) {
	os << "[";
	bool was = false;
	for (const auto& x : v) {
		if (was) {
			os << ", ";
		} else {
			was = true;
		}
		os << x;
	}
	os << "]";
	return os;
}

template<class T>
T sqr(const T& x) {
	return x * x;
}

//////////////////////////////////////////////



void solve() {
	int n, k;
	cin >> n >> k;
	ld u;
	cin >> u;
	vector < ld > a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a.begin(), a.end());
	const ld eps = 1e-12;
	while (u > eps) {
		int j = 1;
		while (j < n && abs(a[j] - a[0]) < eps) {
			j++;
		}
		ld nxt = 1;
		if (j < n) {
			nxt = a[j];
		}
		ld x = u / j;
		if (x >= (nxt - a[0])) {
			x = nxt - a[0];
		}
		u -= x * j;
		ld dop = a[0] + x;
		for (int i = 0; i < j; i++) {
			a[i] = dop;
		}
	}
	ld ans = 1;
	for (int i = 0; i < n; i++) {
		ans *= a[i];
	}
	cout.precision(10);
	cout << fixed << ans << "\n";
}

int main() {
#ifdef LOCAL
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//cout << endl << endl;
	
#endif
	
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	
	return 0;

}
