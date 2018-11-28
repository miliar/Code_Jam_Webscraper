#include <bits/stdc++.h>
using namespace std;

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		string s;
		int k;
		cin >> s >> k;
		bool sorry = false;
		int ans = 0;
		for (int i = 0; i < (int) s.size() && !sorry; ++i) {
			for (int j = i; j < (int) s.size(); ++j) {
				if (s[j] == '-') {
					if (j + k > (int) s.size()) {
						sorry = true;
					} else {
						for (int a = j; a < j + k; ++a) {
							s[a] == '+' ? s[a] = '-' : s[a] = '+';
						}
						ans++;
						break;
					}
				}
			}
		}
		printf("Case #%d: ", Case);
		if (sorry) {
			printf("IMPOSSIBLE");
		} else {
			printf("%d", ans);
		}
		if (Case != t)
			putchar('\n');
	}
	return 0;
}
