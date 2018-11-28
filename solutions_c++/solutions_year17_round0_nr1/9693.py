#include <stdio.h>
#include <string.h>

char s[2000];
int K;

void sol() {
	scanf("%s %d", s, &K);
	int len = strlen(s);
	int neg = 0, count = 0;
	for (int i=0; i < len; i++)
		if (s[i] == '-') neg++;
	if (!neg) {
		printf("0\n");
		return;
	}
	for (int i=0; i<len; i++) {
	//	printf("%s\n", s);
		if( s[i] == '+') continue;
		if (len-i < K && neg != 0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		for(int j=0; j<K; j++) {
			if(s[i+j]=='+') {
				s[i+j]='-';
				neg++;
			}else {
				s[i+j]='+';
				neg--;
			}
		}
		count ++;
	}
	printf("%d\n", count);
	return;
}
int main() {
	int T;
	scanf("%d", &T);

	for (int i=1; i<=T; i++) {
		printf("Case #%d: ", i);
		sol();
	}

	return 0;
}