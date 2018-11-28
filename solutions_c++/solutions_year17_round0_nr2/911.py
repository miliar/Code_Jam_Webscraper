#include <bits/stdc++.h>
using namespace std;

void gettl(bool b) {
	int crt = 1;
	if (!b) {
		for (int i = 0; i < (int) 2e9; i++) {
			crt *= 17;
		}
		gettl(false);
	}
}

#ifndef _DEBUG
#define ass(_Expr) ((void)0)
#define dout(...) ((void)0)
#else
#define dout(...) cout << __VA_ARGS__; cout.flush()
#define ass(_Expr) assert(_Expr);
#endif

typedef long long ll;
typedef double ld;
const int INF = 2e9;
const ll LINF = 2e18;
const ll MOD = 1e9 + 9;
const int PRIME = 29;
const ld EPS = 1e-10;
const ld PI = 3.14159265358979323846;

void solve() {
	string target;
	cin >> target;
	target.insert(target.begin(), '0');
	string::iterator it = target.begin();
//	cerr << target << " begin\n";
	while (it + 1 != target.end()) {
		if (*it > *(it + 1)) {
			(*it)--;
			fill(it + 1, target.end(), '9');
			it--;
		} else {
			it++;
		}
//		cerr << target << " " << it - target.begin() << "\n";
	}
	while (target.front() == '0') {
		target.erase(target.begin());
	}
	cout << target << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
//	freopen("keepcounted.in", "r", stdin);
//	freopen("keepcounted.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cout << "CASE #" << tt + 1 << ": ";
		solve();
	}
	return 0;
}
