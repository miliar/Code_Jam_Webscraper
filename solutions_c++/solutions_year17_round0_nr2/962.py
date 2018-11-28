#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int main() {
	int _t;

	scanf("%d", &_t);

	char s[155];

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		scanf("%s", s);

		int n = strlen(s);
		int last = 0;

		vector<int> a(n);

		for (int i = 0; i < n; i++) a[i] = s[i] - '0';

		for (int i = 0; i < n; i++) {
			if (a[i] < last) {
				a[i] = 9;

				for (int j = i; j < n; j++) a[j] = 9;

				a[i - 1]--;

				for (int j = i - 1; j >= 0; j--) {
					if (a[j] < 0) {
						a[j] += 10;
						if (j - 1 >= 0) a[j - 1]--;
					} else break;
				}

				last = 0;
				i = -1;
				continue;
			}

			last = a[i];
		}

		bool flag = false;

		for (int i = 0; i < n; i++) {
			if (a[i] != 0) flag = true;
			if (flag) printf("%d", a[i]);
		}

		puts("");
	}

	return 0;
}

