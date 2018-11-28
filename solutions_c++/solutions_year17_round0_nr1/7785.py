#include <bits/stdc++.h>

using namespace std;

void flip(string& s, int pos, int k) {
	for (int i = 0; i < k; ++ i) {
		s[pos + i] = s[pos + i] == '+' ? '-' : '+';
	}
}

int main() {
	int tes;

	cin >> tes;
	for (int tcase = 1; tcase <= tes; ++ tcase) {
		string s;
		int k;

		cin >> s >> k;

		int ans = 0;
		for (int i = 0; i <= s.size() - k; ++ i) {
			if (s[i] == '-') {
				flip(s, i, k);
				ans += 1;
			}
		}

		bool solution = true;
		for (int i = 0; i <= s.size(); ++ i) {
			if (s[i] == '-') {
				solution = false;
				break;
			}
		}

		printf("Case #%d: ", tcase);
		if (solution) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}

	}

	return 0;
}