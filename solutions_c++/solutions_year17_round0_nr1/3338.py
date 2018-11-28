#include <bits/stdc++.h>
using namespace std;
#define ll long long

char flip(char c) {
	if(c == '-') return '+';
	else return '-';
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);

	int T;cin >> T;
	string s;int k;
	for(int t=1;t<=T;++t) {
		cin >> s >> k;
		int ans = 0,i = 0;
		while(i < s.size()) {
			if(s[i] == '-') {
				if(i + k > s.size()) {
					ans = -1;
					break;
				}
				for(int j=0;j<k;++j) s[i + j] = flip(s[i + j]);
				ans++;
			}
			i++;
		}
		if(ans != -1)
			cout << "Case #" << t << ": " << ans << endl;
		else
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}
}
