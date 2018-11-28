#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++) {
		char s[25];
		scanf("%s", s);
		int l = strlen(s);
		for(int i = 1; i < l; i++) {
			if(s[i] < s[i-1]) {
				char c = s[i-1];
				int j;
				for(j = i-1; j >= 0 && s[j-1] == c; j--);
				s[j]--;
				for(int k = j+1; k < l; k++)
					s[k] = '9';
				break;
			}
		}
		printf("Case #%d: ", cas);
		bool zero = true;
		for(int i = 0; i < l; i++) {
			if(s[i] != '0' || !zero) {
				printf("%c", s[i]);
				zero = false;
			}
		}
		puts("");
	}
}