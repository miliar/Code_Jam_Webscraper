#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

void solve(int testid) {
	string s;
	cin >> s;

	const int n = s.size();

	if (is_sorted(s.begin(), s.end())) {
		printf("Case #%d: %s\n", testid, s.data());
		return;
	}

	int j = 0;
	for (int i = 0; i + 1 < n; i++) {
		if (s[i] > s[i + 1]) {
			break;
		}
		if (s[i] < s[i + 1]) {
			j = i + 1;
		}
	}

	s[j]--;
	for (int i = j + 1; i < n; i++) {
		s[i] = '9';
	}
	if (s[0] == '0') {
		s.erase(s.begin());
	}

	printf("Case #%d: %s\n", testid, s.data());
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}