#include <iostream>
#include <string>

using namespace std;

void flip(string *s, int from, int k) {
	for (int i = from; i < from + k; ++i) {
		(*s)[i] = ((*s)[i] == '+') ? '-' : '+';
	}
}

void main() {
	int tn, n, m;
	cin >> tn;

	for (int t = 1; t <= tn; ++t) {
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();

		int res = 0;

		for (int i = 0; i < n - k + 1; ++i) {
			if (s[i] == '-') {
				res++;
				flip(&s, i, k);
			}
		}

		bool ok = true;
		for (int i = n - k + 1; i < n; ++i) {
			if (s[i] != '+') {
				ok = false;
				break;
			}
		}
		if (ok) {
			cout << "Case #" << t << ": " << res << endl;
		}
		else {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		}

	}
}