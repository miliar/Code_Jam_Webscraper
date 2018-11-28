#include <bits/stdc++.h>

using namespace std;

void solve(int t_num) {
	string s;
	cin >> s;
	int len = s.size();
	string ans = "";
	for(int i = 1; i <= len; ++i) {
		int dig = -1;
		for(int j = 1; j <= 9; ++j) {
			string cur = ans;
			for(int k = 1; k <= len - i + 1; ++k)
				cur += j + '0';
			if(cur <= s)	
				dig = j;
		}
		if(dig != -1)
			ans += dig + '0';
		else
			break;
	}
	if(ans == "") {
		for(int i = 1; i < len; ++i)
			ans += '9';
	}
	cout << "Case #" << t_num << ": ";
	cout << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		solve(i);
	}

	return 0;
}