#include <cstdio>
#include <cstring>
#include <iostream>

#define MaxN 10010

int T;
char str[MaxN];

int main() {
	scanf("%d", &T);
	int T0 = 0;
	for ( ; T; --T) {
		scanf("%s", str);
		int lastpos = 0, len = strlen(str);
		for (int i = 0; i + 1 < len; ++i) {
			if (str[i] > str[i + 1]) {
				str[lastpos]--;
				for (int j = lastpos + 1; j < len; ++j)
					str[j] = '9';
				break;
			}
			else if (str[i] < str[i + 1]) {
				lastpos = i + 1;
			}
		}
		bool flag = false;
		printf("Case #%d: ", ++T0);
		for (int i = 0; i < len; ++i) {
			if (str[i] == '0' && !flag)
				continue;
			flag = true;
			printf("%c", str[i]);
		}
		puts("");
	}
}