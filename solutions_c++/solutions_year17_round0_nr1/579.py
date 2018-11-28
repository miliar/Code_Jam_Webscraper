#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll n, m, t, k, ans;
vector<ll> a;
string s;

int main() {
	cin >> t;

	for(int x = 1; x <= t; x++) {
		cin >> s >> k;

		ans = 0;
		for(int i = 0; i+k-1 < s.size(); i++) {
			//cout << s << " ";
			if(s[i]=='-') {
				ans++;
				for(int j = i; j < i+k; j++) {
					if(s[j]=='-') s[j] = '+';
					else s[j] = '-';
				}
			}
			if(s[s.size()-1-i]=='-') {
				ans++;
				for(int j = i; j < i+k; j++) {
					if(s[s.size()-1-j]=='-') s[s.size()-1-j] = '+';
					else s[s.size()-1-j] = '-';
				}
			}
			//cout << s << endl;
		}


		bool is = 1;
		for(int i = 0; i < s.size(); i++) {
			if(s[i]=='-') {
				is = 0;
			}
		}

		cout << "Case #" << x << ": ";
		if(is) cout << ans << endl;
		else cout << "IMPOSSIBLE\n";
	}
}