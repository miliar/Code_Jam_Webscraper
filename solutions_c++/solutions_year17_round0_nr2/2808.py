#include <bits/stdc++.h>

using namespace std;

int t;

string n;
int main () {
	scanf("%d", &t);
	for (int tt = 0; tt < t; ++tt) {
		cin >> n;

		bool cont = true;

		while (cont) {
			cont = false;
			for (int i = 0; i < n.length() - 1; ++i) {
				if (n[i] > n[i + 1]) {
					n[i]--;
					cont = true;
					for (++i; i < n.length(); ++i) {
						n[i] = '9';
					}
				}
			}
		}

		int pos = 0;
		while (n[pos] == '0') {
			pos++;
		}

		cout << "Case #" << tt + 1 << ": " << n.substr(pos) << endl;
	}

}