#include <bits/stdc++.h>
using namespace std;

string s, ans;

bool lessThan(string& s1, string& s2) {
	for (int i = 0; i < (int) s1.size(); i++) {
		if (s1[i] < s2[i])
			return true;
		else if (s1[i] > s2[i])
			return false;
	}
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int l = 1; l <= t; l++) {
		bool flag = false;
		cin >> s;
		ans.resize(s.size());
		for (int i = 0; i < (int) s.size(); i++) {
			for (int j = i; j < (int) s.size(); j++) {
				ans[j] = s[i];
			}
			if (!lessThan(ans, s)) {
				ans[i] = s[i] - 1;
				if (s[i] == '1')
					flag = true;
				for (int j = i + 1; j < (int) s.size(); j++) {
					ans[j] = '9';
				}
				break;
			}
		}
		printf("Case #%d: ", l);
		for (int i = flag; i < (int) ans.size(); i++) {
			printf("%c", ans[i]);
		}
		printf("\n");
	}

	return 0;
}
