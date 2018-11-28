#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, i, j, k, ans, cases = 1;
	string s;
	cin>>t;
	while(t--) {
		ans = 0;
		cin>>s>>k;
		for(i = 0; i <= s.length() - k; i++) {
			if(s[i] == '-') {
				for(j = i; j < i + k; j++) {
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
		}
		for(i = 0; i < s.length(); i++) {
			if(s[i] == '-') break;
		}
		if(i == s.length()) cout<<"Case #"<<cases<<": "<<ans<<"\n";
		else cout<<"Case #"<<cases<<": IMPOSSIBLE\n";
		cases++;
	}
	return 0;
}