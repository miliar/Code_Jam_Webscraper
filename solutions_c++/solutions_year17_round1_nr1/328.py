#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

char buf[26][26];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int R, C;
		scanf("%d%d", &C, &R);
		for (int i = 0; i < C; i++) {
			scanf(" %s", buf[i]);
		}
		bool blank = true;
		for (int i = 0; i < C; i++) {
			char cur = '?';
			for (int j = 0; j < R; j++) {
				if (buf[i][j] == '?') {
					buf[i][j] = cur;
				} else {
					if (cur == '?') {
						for (int k = 0; k < j; k++) {
							buf[i][k] = buf[i][j];
						}
					}
					cur = buf[i][j];
				}
			}
			if (cur == '?') {
				if (!blank) {
					strcpy(buf[i], buf[i - 1]);
				}
			} else {
				if (blank) {
					for (int k = 0; k < i; k++) {
						strcpy(buf[k], buf[i]);
					}
				}
				blank = false;
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < C; i++) {
			printf("%s\n", buf[i]);
		}
	}
	return 0;
}
