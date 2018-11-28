#include <bits/stdc++.h>
using namespace std;

char s[30][30];
char u[30][30];
int n, m;

void solve(int t_num) {
	scanf("%d %d", &n, &m);
	for(int i = 0; i < n; ++i)
		scanf("%s", s[i]);
	memset(u, 0, sizeof u);
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j < m; ++j) {
			if(!u[i][j] && s[i][j] != '?') {
				u[i][j] = 1;
				for(int k = j - 1; k >= 0 && !u[i][k] && s[i][k] == '?'; --k)
					u[i][k] = 1, s[i][k] = s[i][j];
				for(int k = j + 1; k < m && !u[i][k] && s[i][k] == '?'; ++k)
					u[i][k] = 1, s[i][k] = s[i][j];
			}
		}
		
		if(i > 0)
		for(int j = 0; j < m; ++j) {
			if(s[i][j] == '?') {
				s[i][j] = s[i-1][j];
			}
		}
	}
	for(int i = n - 2; i >= 0; --i) {
		for(int j = 0; j < m; ++j) {
			if(s[i][j] == '?') {
				s[i][j] = s[i+1][j];
			}
		}
	}
		
	printf("Case #%d:\n", t_num);
	for(int i = 0; i < n; ++i)
		printf("%s\n", s[i]);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		solve(i);
	}
	return 0;
}