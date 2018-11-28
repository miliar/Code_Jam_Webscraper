#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 25;

char a[N][N + 1];
int n, m;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", a[i]);
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == '?') {
					continue;
				}
				for (int k = j - 1; k >= 0; --k) {
					if (a[i][k] == '?') {
						a[i][k] = a[i][j];
					} else {
						break;
					}
				}
			}
			for (int j = m - 1; j >= 0; --j) {
				if (a[i][j] == '?') {
					continue;
				}
				for (int k = j + 1; k < m; ++k) {
					if (a[i][k] == '?') {
						a[i][k] = a[i][j];
					} else {
						break;
					}
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			bool empty = true;
			for (int j = 0; j < m; ++j) {
				if (a[i][j] != '?') {
					empty = false;
					break;
				}
			}
			if (!empty) {
				for (int k = i - 1; k >= 0; --k) {
					bool blank = true;
					for (int j = 0; j < m; ++j) {
						if (a[k][j] != '?') {
							blank = false;
							break;
						}
					}
					if (blank) {
						strcpy(a[k], a[i]);
					} else {
						break;
					}
				}
				for (int k = i + 1; k < n; ++k) {
					bool blank = true;
					for (int j = 0; j < m; ++j) {
						if (a[k][j] != '?') {
							blank = false;
							break;
						}
					}
					if (blank) {
						strcpy(a[k], a[i]);
					} else {
						break;
					}
				}
			}
		}

		printf("Case #%d:\n", _);
		for (int i = 0; i < n; ++i) {
			printf("%s\n", a[i]);
		}
	}
	return 0;
}
