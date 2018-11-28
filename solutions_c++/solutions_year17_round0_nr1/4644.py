#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <queue>


using namespace std;


int solve(string &s, int k) {
	int ret = 0;
	for (int i = 0; i + k <= s.length(); i++) {
		if (s[i] == '+')continue;
		++ret;
		for (int j = i; j < i + k; j++) {
			if (s[j] == '+')s[j] = '-'; else s[j] = '+';
		}
	}
	string t = "";
	for (int i = 0; i < s.length(); i++)t += "+";
	if (s == t) return ret; else return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tcs;
	cin >> tcs;
	for (int i = 1; i <= tcs; ++i) {
		string s;
		int k;
		cin >> s >> k;
		int res = solve(s, k);
		if (res == -1) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i << ": " << res << endl;
		}
	}


	return 0;
}

