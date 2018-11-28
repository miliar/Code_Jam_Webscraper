#include <bits/stdc++.h>

using namespace std;

int main() {
	int tc;
	cin >> tc;

	for (int i = 1; i <= tc; ++i) {
		int k, blank = 0, steps = 0;
		string s;
		cin >> s >> k;

		for (size_t j = 0; j < s.size(); ++j)
			blank += s[j] == '-' ? 1 : 0;

		for (size_t j = 0; j < s.size()-k+1; ++j) {
			if (blank == 0) break;
			if (s[j] == '-') {
				for (int a = 0; a < k; a++) {
					s[j+a] = s[j+a] == '-' ? '+' : '-';
					blank += s[j+a] == '+' ? -1 : 1;
				}
				steps++;
			}
		}

		cout << "Case #" << i << ": ";
		if (blank) cout << "IMPOSSIBLE\n";
		else cout << steps << '\n';
	}
}