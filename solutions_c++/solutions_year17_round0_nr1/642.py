#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <bitset>

using namespace std;

const int MAX_TIMES = 2000; // 125 * 9 + 1あれば 十分


long long solve(string s, int k) {
	int n_flip = 0;
	for (int i = 0; i <= s.size() - k; i++) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; j++) {
				s[j] = s[j] == '+' ? '-' : '+';
			}
			n_flip++;
		}
	}

	return s.find('-') == string::npos ? n_flip : -1;
}

int main() {
	int t, k;
	string s;

	cin >> t;
	vector<int> ans(t, 0);

	for (int i = 0; i < t; i++) {
		cin >> s >> k;
		ans[i] = solve(s, k);
	}

	for (int i = 0; i < t; i++) {
		if (ans[i] == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		} else {
			printf("Case #%d: %d\n", i + 1, ans[i]);
		}
	}
	return 0;
}
