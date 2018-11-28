#include<stdio.h>
#include<string.h>
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int tc = 0;

	char s[1000];
	while (t--) {
		scanf("%s", s);
		int l = strlen(s);
		int cnt = 0;
		for (int i = 1;i < l;i++) {
			if (s[i] < s[i - 1]) {
				cnt++;
			}
		}
		if (cnt == 0) {
			printf("Case #%d: ", ++tc);
			for (int i = 0;i < l;i++) printf("%c", s[i]);
			printf("\n");
			continue;
		}
		int idx = l - 1;
		for (int i = l-1;i >= 1;--i) {
			if (s[i] < s[i - 1]) {
				s[i - 1]--;
				idx = i-1;
			}
		}

		if (idx != 0&&s[0]!='0') {
			for (int i = idx+1;i < l;i++) s[i] = '9';
			
			printf("Case #%d: ", ++tc);
			for (int i = 0;i < l;i++) printf("%c", s[i]);
			printf("\n");
		}
		else {
			if (s[0] == '0') {
				for (int i = 0;i < l - 1;i++) {
					s[i] = '9';
				}

				printf("Case #%d: ", ++tc);
				for (int i = 0;i < l-1;i++) printf("%c", s[i]);
				printf("\n");
			}
			else {
				for (int i = idx + 1;i < l;i++) s[i] = '9';
				printf("Case #%d: ", ++tc);
				for (int i = idx;i < l;i++) printf("%c", s[i]);
				printf("\n");
			}
				
		}
	}
	return 0;
}