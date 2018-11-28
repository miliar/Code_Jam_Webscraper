#include <bits/stdc++.h>

void solve(std::string &s, std::string &ans) {
	int n = (int)s.size();
	
	int firstDiff = -1;
	for (int i = 1; i < n; i++) {
		if (s[i - 1] > s[i]) {
			firstDiff = i - 1;
			break;
		}
	}
	
	if (firstDiff == -1) {
		ans = s;
		return;
	}
	
	while (true) {
		s[firstDiff]--;
		if (firstDiff == 0) {
			if (s[firstDiff] >= '1') {
				break;
			} else {
				for (int i = firstDiff + 1; i < n; i++) {
					ans += '9';
				}
				return;
			}
		}
		
		if (s[firstDiff] >= s[firstDiff - 1]) break;
		firstDiff--;
	}
	
	ans = s.substr(0, firstDiff + 1);
	for (int i = firstDiff + 1; i < n; i++) {
		ans += '9';
	}
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		std::string s; std::cin >> s;
		
		std::string ans;
		solve(s, ans);
		
		printf("Case #%d: %s\n", i, ans.c_str());
	}

	return 0;
}
