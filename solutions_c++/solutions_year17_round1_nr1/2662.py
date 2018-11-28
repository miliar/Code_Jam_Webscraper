#include <bits/stdc++.h>
using namespace std;

char s[20][20];

int main() {
	int t , kase = 0;
	scanf("%d" , &t);
	for( ; t--; ) {
		int n , m;
		scanf("%d%d" , &n , &m);
		for(int i = 0; i < n; i++) {
			scanf("%s" , s[i]);
		}

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(s[i][j] != '?') {
					for(int k = j - 1; k >= 0 && s[i][k] == '?'; k--) {
						s[i][k] = s[i][j];
					}
					for(int k = j + 1; k < m && s[i][k] == '?'; k++) {
						s[i][k] = s[i][j];
					}
				}
			}
		}

		for(int i = 0; i < n; i++) {
			int ok = 0;
			for(int j = 0; j < m; j++) {
				if(s[i][j] != '?') ok = 1;
			}

			if(ok) {
				for(int j = i - 1; j >= 0 && s[j][0] == '?'; j--) {
					for(int k = 0; k < m; k++) {
						s[j][k] = s[i][k];
					}
				}
				for(int j = i + 1; j < n && s[j][0] == '?'; j++) {
					for(int k = 0; k < m; k++) {
						s[j][k] = s[i][k];
					}
				}
			}
		}

		printf("Case #%d:\n" , ++kase);
		for(int i = 0; i < n; i++) {
			printf("%s\n" , s[i]);
		}
	}
	return 0;
}