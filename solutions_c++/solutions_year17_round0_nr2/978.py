#include <bits/stdc++.h>

using namespace std;

int T, n;
char s[20], res[20];

bool check() {
	for(int i = 1; i < n; i ++) {
		if(res[i] < res[i-1]) {
			return 0;
		}
	}
	return 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> s;
		n = strlen(s);
		
		memset(res, 0, sizeof(res));
		for(int i = n; i >= 0; i --) {
			if(i == n) {
				for(int j = 0; j < n; j ++) {
					res[j] = s[j];
				}
				if(check()) {
					break;
				}
			} else {
				if(s[i] == '0') {
					continue;
				}
				for(int j = 0; j <= i; j ++) {
					res[j] = s[j];
				}
				res[i] --;
				char mx = '9';
				for(int j = n-1; j > i; j --) {
					mx = max(mx, s[j]);
					res[j] = mx;
				}
				if(check()) {
					break;
				}
			}	
		}
		char *pt = res;
		while(*pt == '0') pt ++;
		printf("Case #%d: %s\n", cas, pt);
	} 
	
	return 0;
}

