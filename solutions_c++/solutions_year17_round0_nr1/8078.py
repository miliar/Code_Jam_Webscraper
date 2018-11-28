#include <iostream>
#include <string>
using namespace std;

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++) {
		string s;
		int n, cnt = 0;
		bool flag = 0;
		cin >> s;
		scanf("%d", &n);
		if (s.size() < n) {
			for (int i = 0; i < s.size(); i++) {
				if (s[i] == '-') flag = 1;
			}
			if (flag) printf("Case #%d: IMPOSSIBLE\n", t);
			else printf("Case #%d: %d\n", t, 0);
			continue;
		}
		for (int i = 0; i < s.size() - n + 1; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i; j < i + n; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		for (int i = 0; i < s.size(); i++) if (s[i] == '-') flag = 1;
		if (flag) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, cnt);
	}

	return 0;
}