#include <bits/stdc++.h>
using namespace std;

string s;
int k;
int t;
int ans;

void flip(int p) {
	for (int i=p;i<p+k;++i) {
		if (s[i] == '-') s[i]='+';
		else s[i]='-';
	}
}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	for (int tcs=1;tcs<=t;++tcs) {
		cin >> s >> k;
		ans=0;
		for (int i=0;i+k-1<(int)s.size();++i) {
			if (i==(int)s.size()-k) {
				for (int j=i;j<i+k;++j) {
					if (s[j]=='-') {
						flip(i);
						++ans;
						break;
					}
				}
			}
			else if (s[i]=='-') {
				flip(i);
				++ans;
			}
		}
		for (char c : s) {
			if (c=='-') {
				ans=-1;
				break;
			}
		}
		if (ans==-1) cout << "Case #" << tcs << ": IMPOSSIBLE\n";
		else cout << "Case #" << tcs << ": " << ans << '\n';
	}
	return 0;
}
