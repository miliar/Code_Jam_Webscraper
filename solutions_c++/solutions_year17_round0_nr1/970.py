#include <bits/stdc++.h>
using namespace std;

// why am I so weak

char s[1055];

int main() {
	int _t;

	cin >> _t;

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		scanf("%s", s);

		int k;
		scanf("%d", &k);

		int n = strlen(s);
		int res = 0;

		for (int i = 0; i + k - 1 < n; i++) if (s[i] == '-') {
			res++;

			for (int j = i; j < i + k; j++) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
		}

		bool bad = false;

		for (int i = 0; i < n; i++) if (s[i] == '-') {
			bad = true;
		}

		if (bad) {
			puts("IMPOSSIBLE");
			continue;
		}

		printf("%d\n", res);
	}

	return 0;
}

