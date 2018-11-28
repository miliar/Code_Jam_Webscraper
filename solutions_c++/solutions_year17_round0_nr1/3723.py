#include <bits/stdc++.h>

using namespace std;

string s;
int check() {
	for(int i = 0; i < s.size(); i++) {
		if(s[i] == '-') return 0;
	}
	return 1;
}
int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int t, kase = 1;
	int k;
	cin >> t;
	while(t--) {
		int ans = 0;
		int flag = 1;
		cin >> s >> k;
		int len = s.size();
		for(int i = 0; i < len - k + 1; i++) {
			if(s[i] == '-') {
				for(int j = i; j < i + k; j++) {
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
			if(check()) {
				printf("Case #%d: %d\n", kase++, ans);
				flag = 0;
				break;
			}
		}
		if(flag) printf("Case #%d: IMPOSSIBLE\n", kase++);
	}
	return 0;
}