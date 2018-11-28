//============================================================================
// Name        : tidy.cpp
// Author      : Dick Carter
//============================================================================

#include <iostream>
#include <string>
using namespace std;

using size_type = string::size_type;
string makeTidier(const string &s);
string trimLeadingZeros(const string &s);

int main() {
	int numTests;
	cin >> numTests;
	for (int testId = 1; testId <= numTests; ++testId) {
		cout << "Case #" << testId << ": ";
		string s;
		cin >> s;
		auto tidier_s = makeTidier(s);
		while (tidier_s != s) {
			s = tidier_s;
			tidier_s = makeTidier(s);
		}
		cout << trimLeadingZeros(tidier_s) << endl;
	}
	return 0;
}

int charToNum(char c) {
	return c - '0';
}

int numToChar(int i) {
	return "0123456789"[i];
}

string trimLeadingZeros(const string &s) {
	size_type pos = 0;
	for (;s[pos] == '0'; ++pos)
		;
	return s.substr(pos);
}

string makeTidier(const string &s) {
	string tidier = s;
	size_type strSize = s.size();

	for (size_type i = 0; i < strSize-1; ++i) {
		if (charToNum(tidier[i]) > charToNum(tidier[i+1])) {
			tidier[i] = numToChar(charToNum(tidier[i]) - 1);
			++i;
			for (; i != strSize; ++i)
				tidier[i] = '9';
			break;
		}
	}
	return tidier;
}
