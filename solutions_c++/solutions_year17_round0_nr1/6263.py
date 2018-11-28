#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>

char s[2000];
void run() {
	int k;
	scanf("%s%d", s, &k);
	int len = strlen(s);
	int ans = 0;
	for(int i = 0; i <= len - k; i++) {
		if(s[i] == '-') {
			for(int j = i; j < i + k; j++) 
				s[j] = (s[j] == '-') ? '+' : '-';
			ans++;
		}
	}
	for(int i = 0; i < len; i++) 
		if(s[i] != '+') {
			printf("IMPOSSIBLE\n");
			return ;
		}
	printf("%d\n", ans);
}

int main() {
	int T; 
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		run();
	}
	return 0;
}