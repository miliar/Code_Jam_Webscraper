#include <stdio.h>
#include <string.h>
char s[25];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		int i, ln, j, flg = 0, cn=0;
		scanf("%s", s);
		ln = strlen(s);
		for (i = ln - 1; i >= 0; i--) {
			if (i == 0) {
				if (flg == 1) {
					s[i]--;
				}
				break;
			}
			if (flg == 1) {
				if (s[i] > '1') s[i]--;
				else {
					s[i] = '9';
					flg = 1;
					continue;
				}
				i++;
				flg = 0;
				continue;
			}
			if (s[i] == '0') {
				for (j = i; j < ln; j++) s[j] = '9';
				flg = 1;
			}
			else if (s[i - 1] > s[i]) {
				s[i - 1]--;
				for (j = i; j < ln; j++) s[j] = '9';
			}
		}
		for (i = 0; i < ln; i++) {
			if (s[i] == '0') continue;
			else break;
		}
		cn = i;
		printf("Case #%d: %s\n", t, s + cn);

	}


	return 0;
}