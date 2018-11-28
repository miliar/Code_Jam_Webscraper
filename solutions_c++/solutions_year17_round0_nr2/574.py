#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll n, m, t, k, ans;
vector<ll> a;
string s;

int main() {
	cin >> t;

	for(int x = 1; x <= t; x++) {
		cin >> s;

		for(int i = s.size()-1; i > 0; i--) {
			if(s[i] < s[i-1]) {
				s[i-1]--;
				for(int j = i; j < s.size(); j++) s[j] = '9';
			}
		}
		if(s[0]=='0') s = s.substr(1, s.size()-1);

		cout << "Case #" << x << ": " << s << endl;
	}
}