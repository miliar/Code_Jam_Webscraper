#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int T;
	char s[25];
	
	scanf("%d", &T);
	gets(s);
	for (int times = 1; times <= T; ++times) {
		printf("Case #%d: ", times);
		
		gets(s);
		int l = strlen(s);
		for (int i = 1; i < l; ++i) {
			if (s[i] >= s[i - 1]) {
				continue;
			}
			for (int j = i - 1; j >= 0; --j) {
				if (j == 0 || s[j] - s[j - 1] > 0) {
					s[j] -= 1;
					for (int k = j + 1; k < l; ++k) {
						s[k] = '9';
					}
					break;
				}
			}
			break;
		}
		
		if (s[0] != '0' || l == 1) printf("%c", s[0]);
		for (int i = 1; i < l; ++i) {
			printf("%c", s[i]);
		}
		printf("\n");
	} 
	return 0;
}
