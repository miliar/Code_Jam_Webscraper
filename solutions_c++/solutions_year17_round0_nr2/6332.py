#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int main() {
	int t;
	LL n;
	char s[20];
	scanf("%d", &t);
	for (int caseno = 1; caseno <= t; caseno++) {
		scanf("%lld", &n);
		printf("Case #%d: ", caseno);
		sprintf(s, "%lld", n);
		int len = strlen(s);
		int id = len;
		for (int i = 1; i < len; i++) {
			if (s[i] < s[i-1]) {
				id = i;
				break;	
			}
		}
		
		if (id == len) printf("%s\n", s);	// already sorted
		else {
			char tmp = s[id-1];
			int change;
			for (int i = id-1; i >= 0; i--)
				if (s[i] == tmp) change = i;
			
			s[change]--;
			for (int i = change+1; i < len; i++) {
				s[i] = 9 + '0';
			}
		
			bool leading = 1;
			for (int i = 0; i < len; i++) {
				if (s[i] != '0') {
					printf("%c", s[i]);
					leading = 0;
				}
				else if (!leading) {
					printf("%c", s[i]);
				}
			}
			printf("\n", s);
		}
		
	}
	return 0;
}
