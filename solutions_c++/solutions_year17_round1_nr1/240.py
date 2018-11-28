#include <bits/stdc++.h>

using namespace std;

char s[55][55];

int main() {
	int t;
	int r, c;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; ++i) {
			scanf("%s", s[i]);
		}
		printf("Case #%d:\n", tc);
		for (int i = r - 1; i >= 0; --i) {
			for (int j = c - 1; j >= 0; --j) {
				if (isalpha(s[i][j])) {
					for (int k = j + 1; k < c && s[i][k] == '?'; ++k) {
						s[i][k] = s[i][j];
					}
				}
			}
		}
		for (int i = r - 1; i >= 0; --i) {
			for (int j = c - 1; j >= 0; --j) {
				if (isalpha(s[i][j])) {
					for (int k = j - 1; k >= 0 && s[i][k] == '?'; --k) {
						s[i][k] = s[i][j];
					}
				}
			}
		}
		for (int i = 1; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (s[i][j] == '?')
					s[i][j] = s[i - 1][j];
			}
		}
		for (int i = r - 2; i >= 0; --i) {
			for (int j = 0; j < c; ++j) {
				if (s[i][j] == '?')
					s[i][j] = s[i + 1][j];
			}
		}
		for (int i = 0; i < r; ++i) {
			printf("%s\n", s[i]);
		}
	}
	return 0;
}