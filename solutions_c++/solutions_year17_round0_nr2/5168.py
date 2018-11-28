#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

string solve(string s) {
	string ans = "";
	//forward
	for (int i = 0; i < s.length() - 1; i++) {
		if (s[i] > s[i + 1]) {
			s[i] -= 1;
			for (i += 1; i < s.length(); i++)s[i] = '9';
		}
	}

	//backward
	for (int i = s.length() - 1; i >= 1; i--) {
		if (s[i - 1] > s[i]) {
			for (; i >= 0; i--) {
				s[i] --;
				if (i == 0) {
				}
				else {
					s[i] = '9';
				}
			}
		}
	}
	int offset = s[0] == '0' ? 1 : 0;
	return s.substr(offset, s.length() - offset) ;
}

void output(int num, string arg) {
		cout << "Case #" << num << ": " << arg << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		string s;
		cin >> s;
		output(i, solve(s));
	}
}