#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

char s[50];

int main () {
	
	int t, i = 1;
	
	scanf("%d", &t);
	
	for (int ii = 0; ii < t; ii++) {
		
		scanf(" %s", s);
		
		int n = strlen(s);
		int j, k;
		
		for (j = 0, k = 0; k < n - 1; k++) {
			if (s[k] < s[k + 1]) {
				j = k + 1;
			} else if (s[k] > s[k + 1]) {
				s[j]--;
				/*for (int esp = j; esp <= k; esp++) {
					s[esp]--;
				}*/
				for (int esp = j + 1; esp < n; esp++) {
					s[esp] = '9';
				}
			}
		}
		
		if (s[0] == '0')
			printf("Case #%d: %s\n", i++, s + 1);
		else
			printf("Case #%d: %s\n", i++, s);
	}
	
	return 0;
	
}
