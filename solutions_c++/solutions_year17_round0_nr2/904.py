#include <bits/stdc++.h>
#include <string.h>
#define MAXN 50

using namespace std;

int main(void) {
	char s[MAXN];
	int t;
	
	scanf("%d", &t);

	int tam;
	for(int test = 1; test <= t; test++) {
		scanf("%s", s);
		getchar();
		tam = strlen(s);
		printf("Case #%d: ", test);
		int idx = 0x3f3f3f3f;
		for(int i = tam - 1; i > 0; i--) {
			if(s[i] < s[i-1]) {
				s[i-1]--;
				idx = i;
				s[i] = 9;
			}
		}
		int k = 0;
		while(s[k] == '0') k++;
		while(k < tam) {
			k >= idx ? putchar('9') : putchar(s[k]);
			k++;
		}
		puts("");
	}
	
	
	return 0;
}