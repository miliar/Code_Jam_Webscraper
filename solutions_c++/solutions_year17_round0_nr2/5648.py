#include <iostream>
#include <string>
using std::cin;
using std::cout;

int has_problem(std::string& s, int k) {
	if (k+1 < s.length()) {
		if (s[k] < s[k+1] || (s[k] == s[k+1] && !has_problem(s,k+1)) )
			return false;
		else 
			return true;
	}
	else {
		return false;
	}
}

void fill_with_nine(std::string& s, int k) {
	for (int i = k; i < s.length(); i++) {
		s[i] = '9';
	}
}

void remove_leading_zero(std::string& s) {
	if (s[0] == '0' && s.length() > 1) {
		s.erase(0,1);
	}
}

std::string solve(std::string& s) {
	std::string ans = s;
	
	for (int i = 0; i < ans.length(); i++) {
		if (has_problem(ans,i)) {
			ans[i]--;
			fill_with_nine(ans,i+1);
			break;
		}
	}

	remove_leading_zero(ans);
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		std::string s, sol;
		cin >> s;
		sol = solve(s);
		cout << "Case #" << t << ": " << sol << "\n";
	}
	return 0;
}
