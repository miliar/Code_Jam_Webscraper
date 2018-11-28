#include <bits/stdc++.h>

using namespace std;

int t, w;
string p;

int main () {
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		
		int ans = 0;

		cin >> p >> w;
		for (int i = 0; i < p.length() - w + 1; ++i) {
			if (p[i] == '-') {
				for (int j  =  0; j < w; ++j) {
					p[j + i] = (p[j + i] == '+') ? '-' : '+';
				}
				ans++;
			}
		}

		bool impossible = false;
		for (int i = 0; i < w; ++i) {
			if (p[p.length() - 1 - i] == '-') {
				impossible = true;
				break;
			}
		}

		if (impossible) {
			cout << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl; 
		} else {
			cout << "Case #" << tt + 1 << ": " << ans << endl;
		}
	}
}