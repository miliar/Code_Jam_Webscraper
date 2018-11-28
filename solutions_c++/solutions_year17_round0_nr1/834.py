#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("pancake_outputl.txt", "w", stdout);
	int t; scanf("%d\n", &t);
	string s;
	int n, k, res, mark[1005];
	for(int test = 1; test <= t; test++) {
		cin >> s;
		scanf("%d\n", &k);
		n = s.length();
		for(int i = 0; i <= n; i++) mark[i] = 0;
		res = 0;
		for(int i = 0; i <= n - k; i++) {
			// if (s[i] == '-') {
			// 	++res;
			// 	for(int j = i; j < i + k; j++) {
			// 		if (s[j] == '-') s[j] = '+';
			// 		else s[j] = '-';
			// 	}
			// }
			if (i != 0) mark[i] += mark[i - 1];
			if (mark[i] % 2 == 0) {
				if (s[i] == '-') {
					++mark[i]; 
					++res;
					--mark[i + k];
				}
			}
			else {
				if (s[i] == '+') {
					++mark[i]; 
					++res;
					--mark[i + k];
				}
			}
		}
		for(int i = n - k + 1; i < n; i++) {
			mark[i] += mark[i - 1];
			if ((s[i] == '-' && mark[i] % 2 == 0) || (s[i] == '+' && mark[i] % 2 != 0)) {
				res = -1;
				break;
			}
		}	
		printf("Case #%d: ", test);
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	fclose(stdin);
	fclose(stdout);
}