#include<stdio.h>
#include<string.h>
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int tc = 0;
	while (t--) {
		char s[2000];
		int k;
		scanf("%s %d", s,&k);
		int l = strlen(s);
		int cnt = 0;
		for (int i = 0;i <= l - k;i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i;j < i + k;j++) {
					if (s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		bool flag = true;
		for (int i = 0;i < l;i++) {
			if (s[i] != '+') flag = false;
		}
		if (flag) printf("Case #%d: %d\n", ++tc, cnt);
		else printf("Case #%d: IMPOSSIBLE\n", ++tc);
	}
	return 0;
}