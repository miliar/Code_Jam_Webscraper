#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		string s; int k; cin >> s >> k;
		int ans = 0;
		rep(i, s.size() - k + 1) {
			if (s[i] == '+')continue;
			ans++;
			rep(j, k) {
				if (s[i + j] == '+')s[i + j] = '-';
				else s[i + j] = '+';
			}
		}
		for (char c : s) {
			if (c == '-') { printf("Case #%d: IMPOSSIBLE\n", cnt); goto g; }
		}
		printf("Case #%d: %d\n", cnt, ans);
	g:;
	}
}