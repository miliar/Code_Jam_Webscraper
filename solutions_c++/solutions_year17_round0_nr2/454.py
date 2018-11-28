#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t, T;
char s[1010];
int k;

int main() {
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		int count = 0;
		scanf("%s", s);
		int l = strlen(s);
		for(int i = l - 1; i > 0; i--) {
			if(s[i - 1] > s[i]) {
				for(int j = i; j < l; j++) s[j] = '9';
				s[i - 1]--;
			}
		}
		int x = 0;
		if(s[0] == '0') x = 1;
		printf("Case #%d: %s\n", t, &s[x]);
	}
	return 0;
}
