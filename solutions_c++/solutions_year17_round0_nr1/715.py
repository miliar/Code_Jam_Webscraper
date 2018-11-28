#include<stdio.h>
#include<string.h>
char ch[1004];
int main() {
	int ca;
	scanf("%d", &ca);
	for (int cas = 1; cas <= ca; cas++) {
		int k;
		scanf("%s%d", ch, &k);
		int ct = 0;
		int l = strlen(ch);
		for (int i = 0; i < l; i++) {
			if (ch[i] == '-' && i + k > l) {
				ct = -1;
			} else if (ch[i] == '-') {
				ct++;
				for (int j = 0; j < k; j++) {
					if (ch[i + j] == '-') {
						ch[i + j] = '+';
					} else {
						ch[i + j] = '-';
					}
				}
			}
		}
		if (ct == -1) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else {
			printf("Case #%d: %d\n", cas, ct);
		}
	}
} 
