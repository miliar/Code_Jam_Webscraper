#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin>>tc;
	for (int i=1; i<=tc; i++) {
		string s;
		int k;
		cin>>s>>k;
		int ans=0;
		for (int j=0; j<=s.size()-k; j++) {
			if (s[j]=='-') {
				for (int l=j; l<j+k; l++) {
					s[l]= (s[l]=='+') ? '-' : '+';
				}
				ans++;
			}
		}
		bool allh=true;
		for (int j=0; j<s.size(); j++) allh &= s[j]=='+';
		printf("Case #%d: ", i);
		if (!allh) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}
