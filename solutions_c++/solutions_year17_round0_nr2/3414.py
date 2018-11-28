#include <iostream>
#include <string>

using namespace std;

bool isTidy(string s) {
	int n = s.size();
	if (n == 1) return true;
	for (int i = 0; i < n - 1; i ++) {
		if (s[i] > s[i+1]) return false;
	}
	return true;
}

string minusOne(string  s) {
	//intput: s>= 2 & the first digit is not 0
	//output: the first digit is not 0
	int n = s.size();
	if (s[n - 1] != '0') {
		s[n - 1] = char(int(s[n - 1] - 1));
		return s;
	} else {
		if (n == 2 && s[0] == '1') return "9";
		string result = minusOne(s.substr(0, n - 1));
		result.push_back('9');
		return result;
	}
}

string lastTidy(string s) {
	//input: s >= 1 && the first digit is not 0
	//output: the first digit is not 0
	if (isTidy(s)) return s;
	int n = s.size();
	if (n == 2 && s[0] == '1') return "9";
	string result = minusOne(s.substr(0,n-1));
	result = lastTidy(result);
	result.push_back('9');
	return result;
}

int main() {
	int T;
	cin >> T;
	string s;
	for (int i = 0; i < T; i ++) {
		cin >> s;
		cout << "Case #" << i + 1 << ": " << lastTidy(s) << endl;
	}
	return 0;
}
