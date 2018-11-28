#include <bits/stdc++.h>
using namespace std;

bool check(string s) {
	for (int i = 1; i < s.size(); i++) {
		if (s[i - 1] > s[i]) {
			return false;
		}
	}
	return true;
}

string solve(string s) {
	if (s.size() <= 1) {
		return s;
	}
	string ans = s;
	ans[0] = ans[0] - 1;
	for (int i = 1; i < ans.size(); i++) {
		ans[i] = '9';
	}
	string alter_ans = s.substr(0, 1) + solve(s.substr(1, s.size() - 1));
	if (check(alter_ans)) {
		ans = max(ans, alter_ans);
	}
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for (int t_id = 1; t_id <= t; t_id++) {
		string s;
		cin>>s;
		string ans = solve(s);
		while (ans.size() > 0 && ans[0] == '0') {
			ans = ans.substr(1, ans.size() - 1);
		}
		printf("Case #%d: %s\n", t_id, ans.c_str());
	}

	return 0;
}
