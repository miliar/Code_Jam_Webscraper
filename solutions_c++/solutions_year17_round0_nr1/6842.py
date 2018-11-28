#include <stdio.h>
#include <string.h>
char s[1005];
int k;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		scanf("%s", s);
		scanf("%d", &k);
		int i, ln, j, cnt=0, flg=0;
		ln = strlen(s);
		for (i = 0; i <= ln - k; i++) {
			if (s[i] == '-') {
				cnt++;
				for (j = i; j < i + k; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		for (i = ln - k; i < ln; i++) {
			if (s[i] == '-') flg = 1;
		}
		printf("Case #%d: ", t);
		if (flg == 1) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}