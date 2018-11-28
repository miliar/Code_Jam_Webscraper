#include <bits/stdc++.h>

using namespace std;

void flip(char& c) {
	c = (c == '-' ? '+' : '-');
}

void solve(int id) {
	printf("Case #%d: ", id);

	string s;
	int k;
	cin >> s >> k;

	int fl = 0;
	for (size_t i = 0; i < s.size(); ++i) {
		if (i + k - 1 >= s.size()) {
			break;
		}
		if (s[i] == '-') {
			++fl;
			for (int j = 0; j < k; ++j) {
				flip(s[i + j]);
			}
		}
	}

	for (char c : s) {
		if (c == '-') {
			puts("IMPOSSIBLE");
			return;
		}
	}

	printf("%d\n", fl);
}

int main() {
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		solve(i);
	}

	return 0;
}
