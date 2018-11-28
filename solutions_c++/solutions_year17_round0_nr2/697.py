#include <cstdio>
#include <cstring>

#define SIZE 100

char buf[SIZE];

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int _c = 0; _c < T; _c ++) {
		printf("Case #%d: ", _c + 1);
		scanf("%s", buf);
		int len = strlen(buf);
		for (int i = len - 2; i > -1; i --) {
			if (buf[i] < 0) {
				buf[i] += 10;
				buf[i - 1] -= 1;
			}
			if (buf[i] > buf[i + 1]) {
				buf[i] -= 1;
				for (int j = i + 1; j < len; j ++) {
					buf[j] = '9';
				}
			}
		}
		bool beg = false;
		for (int i = 0; i < len; i ++) {
			if (buf[i] != '0') beg = true;
			if (beg) putchar(buf[i]);
		}
		puts(beg ? "" : "0");
	}
	return 0;
}
