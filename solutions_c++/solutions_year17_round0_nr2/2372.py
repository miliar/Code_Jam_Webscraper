// CodeJam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>

using namespace std;

char tidy(string & s, int end, bool & downgrade)
{
	char c = s[end];
	if (downgrade) {
		if (c == '0') {
			c = '9';
			downgrade = true;
		}
		else{
			c = c - 1;
			downgrade = false;
		}

	}
	if (c < s[end - 1]) {
		downgrade = true;
		return '9';
	}
	else {
		return c;
	}
}

int main()
{
	int t;
	string s, result;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		result = "";
		bool downgrade = false;
		cin >> s;
		//find conflict
		bool conflict = false;
		int st = 1;
		for (st; st < s.size(); ++st) {
			if (s[st-1] > s[st]) {
				conflict = true;
				break;
			}
		}

		if (conflict) {
			for (int end = st; end > 0; end--) {
				result = tidy(s, end, downgrade) + result;
			}
			if (downgrade && s[0] != '1') {
				result = char((s[0] - 1)) + result;
			}
			else if (!downgrade) {
				result = s[0] + result;
			}
			for (int end = st+1; end < s.size(); ++end) {
				result = result + '9';
			}
			cout << "Case #" << i << ": " << result << endl;
		}
		else {
			cout << "Case #" << i << ": " << s << endl;
		}
	}
	//cin >> t;
	return 0;
}

