#include <stdio.h>
#include <string.h>

int t, T;
char s[1010];
int k;

int main() {
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		int count = 0;
		scanf("%s %d", s, &k);
		int l = strlen(s);
		for(int i = 0; i < l; i++) {
			if(s[i] == '-') {
				if(i + k > l) {
					count = -1;
					break;
				}
				for(int j = 0; j < k; j++) {
					s[i + j] = '+' + '-' - s[i + j];
				}
				count++;
			}
		}
		if(count == -1) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, count);
	}
	return 0;
}
