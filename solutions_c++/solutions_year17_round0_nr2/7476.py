#include <bits/stdc++.h>
#define endl '\n'
#define mod 1000000007
typedef long long LL;
const int maxn = 1e5 + 2;
const LL inf = 1e18;
using namespace std;
inline string convert(LL x) {
	string s = "";
	while(x) {
		int d = int(x % 10);
		s.push_back(char(d + '0'));
		x /= 10;
	}
	reverse(s.begin(), s.end());
	return s;
}
inline bool check(string s) {
	bool ok = 1;
	for(int i = 0; i < s.length() - 1; i++) {
		for(int j = i + 1; j < s.length(); j++) {
			if(s[i] > s[j]) ok = 0;
		}
	}
	return ok;
}
inline string solve(string s) {
	for(int i = s.length() - 1; i >= 0; i--) {
		bool ok = 1;
		for(int j = i + 1; j < s.length(); j++) {
			if(s[i] > s[j]) ok = 0;
		}
		if(ok == 1) continue;
		for(int j = i + 1; j < s.length(); j++) s[j] = '9';
		int t = int(s[i] - '0');
		int d = (t? t - 1: 9);
		s[i] = char(d + '0');
		if(!t) {
			int t = int(s[i - 1] - '0');
			int d = (t? t - 1: 9);
			if(i) s[i - 1] = char(d + '0');
		}
	}
	if(s[0] == '0') s = s.substr(1, s.length() - 1);
	return s;
}
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		LL n; cin >> n;
		string s = convert(n);
		if(check(s) == 1) {
			cout << "Case #" << i << ": " << n << endl;
			continue;
		}
		string ans = solve(s);
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
