#include <bits/stdc++.h>

using namespace std;

namespace Solve {

	typedef pair<long, long> pll;
	bool empty[64];
	char mp[64][64];

	void main() {
		ios::sync_with_stdio(false);
		register long i, j;
		long T;
		cin >> T;
		for(long t = 1; t <= T; ++ t) {
			long r, c;
			cin >> r >> c;
			for (i = 0; i < r; ++ i) {
				cin >> mp[i];
				bool e = true;
				for (j = 0; j < c; ++ j) {
					if (mp[i][j] != '?') {
						e = false;
						break;
					}
				}
				empty[i] = e;
			}
			for (i = 0; i < r; ++ i) {
				if (empty[i]) continue;
				for (j = 0;; ++ j) {
					if (mp[i][j] != '?') break;
				}
				char first = mp[i][j];
				for (; j >= 0; -- j) mp[i][j] = first;
				char last = -1;
				for (j = 0; j < c; ++ j) {
					if (mp[i][j] == '?') mp[i][j] = last;
					else last = mp[i][j];
				}
			}
			for (i = 0;; ++ i) {
				if (!empty[i]) break;
			}
			long fr = i;
			for (-- i; i >= 0; -- i) {
				for (j = 0; j < c; ++ j) {
					mp[i][j] = mp[fr][j];
				}
				empty[i] = false;
			}
			for (i = 0; i < r; ++ i) {
				if (empty[i]) {
					for (j = 0; j < c; ++ j) {
						mp[i][j] = mp[fr][j];
					}
				} else {
					fr = i;
				}
			}
			cout << "Case #" << t << ":" << endl;
			for (i = 0; i < r; ++ i) {
				cout << mp[i] << endl;
			}
		}
	}
}

int main(void) {
	Solve::main();
	return 0;
}
