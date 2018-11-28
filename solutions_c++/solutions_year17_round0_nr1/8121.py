#include <cstdio>

int t, k;
char c, s[1005];

int main() {
	scanf("%d", &t);
	for (int ca = 0; ca < t; ca++) {
		scanf("%s%d", s, &k);

		int ans = 0;
		for (int i = 0; i + k < 1005 && s[i + k - 1]; i++){
			if (s[i] == '-') {
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-') {
						s[j] = '+';
					} else {
						s[j] = '-';
					}
				}
				ans++;
			}
		}

		bool sol = true;
		for (int i = 0; s[i]; i++) {
			if (s[i] == '-') sol = false;
		}

		printf("Case #%d: ", ca + 1);
		if (sol) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
