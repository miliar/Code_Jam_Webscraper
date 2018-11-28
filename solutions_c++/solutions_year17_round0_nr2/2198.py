#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

using namespace std;

string get_solution(string &s) {
	char prev = (char)1;
	int crash = -1;
	for (int i = 0; i < s.size(); i++) {
		char cur = s[i];
		if (cur < prev) {
			crash = i;
			break;
		}
		else {
			prev = cur;
		}
	}
	if (crash == -1) {
		return s;
	}
	string ans = "";
	for (int i = 0; i < crash - 1; i++) {
		if (s[i] == s[crash - 1]) {
			crash = i + 1;
			break;
		}
		ans += s[i];
	}
	ans += (char)(s[crash - 1] - 1);
	for (int i = crash; i < s.size(); i++) {
		ans += '9';
	}
	if (ans[0] != '0'){
		return ans;
	}
	else {
		ans = "";
		for (int i = 0; i < s.size() - 1; i++) {
			ans += '9';
		}
		return ans;
	}
}

int main() {
	ios::sync_with_stdio(false);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": " << get_solution(s) << endl;
	}
}