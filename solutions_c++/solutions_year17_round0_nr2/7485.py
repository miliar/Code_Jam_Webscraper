#include <bits/stdc++.h>
using namespace std;

string num_to_s(long long n) {
	string s = "";
	while (n) {
		s += (n%10) + '0';
		n/=10;
	}
	reverse(s.begin(), s.end());
	return s;
}

long long s_to_num(string s) {
	long long x = 0;
	for (int i=0; i<s.length(); i++) {
		x = x*10 + (s[i]-'0');
	}
	return x;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	// your code goes here
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int T=1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		long long n;
		cin >> n;
		string s = num_to_s(n);
		string ans = "";
		for (int i=0; i<s.length(); i++) {
			long long exact = s_to_num(s.substr(i));
			string t = "";
			for (int j=i; j<s.length(); j++) {
				t += s[i];
			}
			long long want = s_to_num(t);
			if (want <= exact) {
				ans += s[i];
			}
			else {
				long long what = (s[i]-'0') - 1;
				ans += (what + '0');
				for (int j=i+1; j<s.length(); j++) ans += '9';
				break;
			}
		}
		while (ans[0] == '0') {
			ans = ans.substr(1);
		}
		cout << ans << endl;
	}
	return 0;
}
