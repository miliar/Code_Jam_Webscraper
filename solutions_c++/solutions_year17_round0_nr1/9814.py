#include<bits/stdc++.h>

using namespace std;

void flip(string &s, int i) {
	if (s[i] == '+') s[i] = '-';
	else s[i] = '+';
}

string s;

int main() {
	int T, n, caso = 0;
	scanf("%d", &T);
	while (T--) {
		cin>>s>>n;
		string s2 = s;
		char c = '-';
		int ans = INT_MAX;

			int temp = 0;
			for(int i=0; i+n<=s.size(); ++i) {
				if (s[i] == c) {
					++temp;
					for(int r=i; r<i+n; ++r) {
						flip(s, r);
					}
				}
			}
			bool ok = 1;
			for(int i=0; i<s.size(); ++i) {
				if (s[i] == c) {
					ok = 0;
				}
			}
			if (ok) ans = min(ans, temp);
		
		printf("Case #%d: ", ++caso);
		if (ans == INT_MAX) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}
