#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		string s;
		int size;
		cin >> s >> size;
		int result = 0;
		for (int i = 0; i < (int)s.size() - size + 1; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < size; ++j) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				++result;
			}
		}
		bool failed = false;
		for (int i = 0; i < (int)s.size(); ++i) {
			failed |= s[i] == '-';
		}
		if (failed) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << result << '\n';
		}
	}

	return 0;
}