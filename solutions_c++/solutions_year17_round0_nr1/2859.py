#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

char s[1010];
int si[1010];
int sum[1010];

int main () {
	
	int t, i = 1;
	
	scanf("%d", &t);
	
	for (int ii = 0; ii < t; ii++) {
		int k;
		
		scanf(" %s %d", s, &k);
		
		int n = strlen(s);
		int j;
		
		for (j = 0; j < n; j++) {
			si[j] = (s[j] == '+' ? 1 : 0);
		}
		int inv = 0;
		int resp = 0;
		for (j = 0; j < n - k + 1; j++) {
			if ((si[j] + inv) % 2 != 1) {
				resp++;
				inv = (inv + 1) % 2;
				sum[j + k - 1] = 1;
			}
			inv = (inv + sum[j]) % 2;
		}
		printf("Case #%d: ", i++);
		for (; j < n; j++) {
			if ((si[j] + inv) % 2 != 1) {
				printf("IMPOSSIBLE\n");
				break;
			}
			inv = (inv + sum[j]) % 2;
		}
		if (j == n) {
			printf("%d\n", resp);
		}
		for (j = 0; j < n; j++) {
			sum[j] = 0;
		}
	}
	
	return 0;
	
}
