#include <bits/stdc++.h>

using namespace std;

namespace Solve {

	typedef pair<long, long> pll;

	map<long, long> r;

	void main() {
		ios::sync_with_stdio(false);
		register long i, j;
		long T;
		cin >> T;
		long n, k;
		for (long t = 1; t <= T; ++ t) {
			cin >> n >> k;
			cout << "Case #" << t << ": ";
			r[n] = 1;
			for (;;) {
				auto it = -- r.end();
				k -= it->second;
				long mx, mi;
				mx = it->first / 2;
				mi = (it->first - 1) / 2;
				if (k <= 0) {
					cout << mx << " " << mi << endl;
					break;
				}
				r[mx] += it->second;
				r[mi] += it->second;
				r.erase(it);
			}
			r.clear();
		}
	}
}

int main(void) {
	Solve::main();
	return 0;
}
