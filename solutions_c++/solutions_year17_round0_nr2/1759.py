#include<cstdio>
#include<string.h>
#define INF 99999999
int T, K, len, ans;
char c, S[20];
int main() {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		ans = len = 0;
		scanf("%s", S);
		len = strlen(S);
		for(int i = len-1; i > 0; i--) {
			if(S[i-1] > S[i]) {
				S[i-1] = (S[i-1] > '0') ? S[i-1]-1 : '9';
				for(int j = i; j < len; j++) {
					S[j] = '9';
				}
			}
		}
		
		printf("Case #%d: %s\n", t, S[0] == '0' ? S+1 : S);
	}
	return 0;
}
