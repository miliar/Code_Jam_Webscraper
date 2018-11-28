#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

int T, K;
string s;
inline void solve() {
	scanf("%d\n", &T);
	for(int ii = 1; ii <= T; ii++) {
		cin >> s;
		scanf("%d\n", &K);
		int tot = 0;
		bool ok = 1;
		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') {
				if(i + K - 1 >= (int)s.size()) {
					ok = 0;
					break;
				}
				tot++; ///
				for(int j = i; j <= i + K - 1; j++) {
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		printf("Case #%d: ", ii);
		if(!ok) printf("IMPOSSIBLE\n");
		else printf("%d\n", tot);
	}
}
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	solve();
	return 0;
}
