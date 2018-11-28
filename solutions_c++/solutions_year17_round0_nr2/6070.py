#include <bits/stdc++.h>
#define ull unsigned long long
#define PB push_back
#define MOD 1000000007
using namespace std;

bool isRight(string & s) {
	for (int i = 1; i < s.size(); i++) {
		if (s[i] < s[i-1])
			return false;
	}
	return true;
}


string solve(string & s) {
	bool flag = false;
	for (int i = 1; i < s.size(); i++) {
		if (flag && s[i-1] == '9') {
			s[i] = '9';
		} else {
			if (s[i] >= s[i-1]) {
				continue;
			} else {
				s[i-1]--;
				s[i] = '9';
				flag = true;
			}
		}
	}
	
	string ans = "";
	flag = false;
	int i;
	for (i = 0; i < s.size(); i++) {
		if (s[i] == '0') {
			continue;
		} else {
			break;
		}
	}
	i = i < s.size() ? i : 0;
	ans = s.substr(i);

	while (!isRight(ans)) {
		ans = solve(ans);
	}
	
	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		string s; cin >> s;
		cout << "Case #" << (i+1) << ": " << solve(s) << "\n"; 
	}
	return 0;
}
