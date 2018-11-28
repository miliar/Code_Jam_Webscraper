#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m;
char buf[33][33];

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++ i) {
			scanf("%s", buf[i]);
		}
		int r = 0;
		while (true) {
			bool flag = false;
			for (int j = 0; j < m; ++ j) {
				if (buf[r][j] != '?') {
					flag = true;
				}
			}
			if (flag) {
				break;
			} else {
				++ r;
			}
		}
		for (int i = r; i < n; ++ i) {
			char last = 0;
			for (int j = 0; j < m; ++ j) {
				if (buf[i][j] == '?') {
					if (last != 0) {
						buf[i][j] = last;
					}
				} else {
					last = buf[i][j];
				}
			}
			last = 0;
			for (int j = m - 1; j >= 0; -- j) {
				if (buf[i][j] == '?') {
					if (last != 0) {
						buf[i][j] = last;
					}
				} else {
					last = buf[i][j];
				}
			}
			if (last == 0) {
				for (int j = 0; j < m; ++ j) {
					buf[i][j] = buf[i - 1][j];
				}
			}
		}
		for (int i = 0; i < r; ++ i) {
			for (int j = 0; j < m; ++ j) {
				buf[i][j] = buf[r][j];
			}
		}
		printf("Case #%d:\n", kase);
		for (int i = 0; i < n; ++ i) {
			puts(buf[i]);
		}
	}
	return 0;
}
