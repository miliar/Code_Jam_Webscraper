#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, k;
	char s[1500];
	scanf("%d", &t);
	for (int caseno = 1; caseno <= t; caseno++) {
		scanf("%s %d", s, &k);
		printf("Case #%d: ", caseno);
		int len = strlen(s);
		int ans = 0;
		for (int i = 0; i < len-k+1; i++) {
			if (s[i] == '-') {
				ans++;
				for (int j = i; j < i+k; j++) {
					if (s[j] == '-') s[j] = '+';
					else if (s[j] == '+') s[j] = '-';	
				}
			}
		}
		
		bool posib = true;
		for (int i = len-k+1; i < len; i++)
			if (s[i] == '-') posib = false;
		
		
		if (posib) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
		
	return 0;
}
