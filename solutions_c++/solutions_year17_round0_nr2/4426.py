#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t;

	scanf("%d", &t);

	for (int id = 1; id <= t; id++) {
		printf("Case #%d: ", id);
		char s[20], ans[20];

		scanf("%s", s);
		int l = strlen(s), descPos = -1;
		for (int i = 0; i < l - 1; i++) {
			if (s[i] > s[i + 1]) {
				descPos = i;
				break;
			}
		}

		strcpy(ans, s);
		if (descPos != -1) {
			for (int i = descPos + 1; i < l; i++) ans[i] = '9';
			ans[descPos] = ans[descPos] - 1;
			while (descPos > 0 and ans[descPos - 1] > ans[descPos]) {
				ans[descPos] = '9';
				descPos--;
				ans[descPos] = ans[descPos] - 1;
			}

			if (ans[0] == '0') {
				for (int i = 0; i < l; i++) ans[i] = ans[i + 1];
			}
		}

		printf("%s\n", ans);
	}
	return 0;
}