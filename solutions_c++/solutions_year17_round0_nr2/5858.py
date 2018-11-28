#include <cstdio>
#include <cstring>

int T;
char a[30];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", a+1);
		int len = strlen(a+1);
		for (int i = 1; i <= len; i++)a[i] -= '0';
		for (int i = len; i > 1; i--) {
			if (a[i] < a[i - 1]) {
				a[i - 1]--;
				a[i] = 9;
			}
			int p = i;
			while (a[p] > a[p + 1] && (p + 1) <= len) {
				a[p + 1] = 9;
				p++;
			}
		}
		printf("Case #%d: ", t);
		for (int i = 1; i <= len; i++) {
			if (a[i])printf("%d", a[i]);
		}
		printf("\n");
	}
	return 0;
}