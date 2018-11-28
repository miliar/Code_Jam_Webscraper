#include<stdio.h>
#include<string.h>

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, test;
	scanf("%d", &test);
	for (t = 1; t <= test; t++) {
		char s[100] = { 0 };
		int len, i, pos[100] = { 0 };
		bool flag = false;
		scanf("%s", s);
		len = strlen(s);
		if (len == 1) {
			printf("Case #%d: %s\n", t, s);
			continue;
		}
		for (i = len - 1; i >= 0; i--) {
			if (i == 0) {
				if (pos[i + 1] == 0) pos[i] = 1;
				else pos[i] = 2;
				break;
			}
			if (s[i - 1] > s[i]) pos[i] = 0;
			else if (s[i - 1] == s[i]) {
				if (i != len - 1 && pos[i + 1] == 0) pos[i] = 0;
				else pos[i] = 2;
			}
			else {
				if (i != len - 1 && pos[i + 1] == 0) pos[i] = 1;
				else pos[i] = 2;
			}
		}
		printf("Case #%d: ", t);
		for (i = 0; i < len; i++) {
			if (flag) {
				printf("9");
				continue;
			}
			if (pos[i] == 2) printf("%c", s[i]);
			else if (pos[i] == 1) {
				if(i != 0 || s[i] != '1')
					printf("%c", s[i] - 1);
				flag = true;
			}
		}
		printf("\n");
	}
	return 0;
}