#include <iostream>
//#include "stdio.h"
#include <string>
#include <algorithm>
using namespace std;


int main() {
	int t;
	cin >> t;

	int n, p;
	int g[120];
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n >> p;
		int c[4] = { 0,0,0,0 };
		for (int i = 0; i < n; ++i) {
			cin >> g[i];
			++ c[g[i] % p];
		}
		cout << "Case #" << tcount << ": ";
		
		int ans = 0;
		int c1 = 0, c2 = 0, c3 = 0;
		if (p == 2) {
			ans = c[0] + (n - c[0] + 1) / 2;
		}
		else if (p == 3) {
			ans += c[0];
			int tp = min(c[1], c[2]);
			ans += tp;
			ans += (max(c[1], c[2]) - tp + 2) / 3;
		}

		cout << ans << endl;
	}

	return 0;
}