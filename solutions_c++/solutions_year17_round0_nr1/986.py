#include <bits/stdc++.h>

using namespace std;

int T, n, k, res, a[1010];
char s[1010];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> s >> k;
		n = strlen(s);
		for(int i = 0; i < n; i ++) a[i] = (s[i] == '+');
		res = 0;
		for(int i = 0; i <= n-k; i ++) {
			if(a[i] == 0) {
				for(int j = 0; j < k; j ++) {
					a[i+j] ^= 1;
				}
				res ++;
			}
		}
		int ok = 1;
		for(int i = 0; i < n; i ++) if(a[i] == 0) {
			ok = 0;
		}
		if(!ok) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else {
			printf("Case #%d: %d\n", cas, res);
		}
	} 
	
	return 0;
}

