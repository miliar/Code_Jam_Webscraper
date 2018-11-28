// Google Code Jam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>

using namespace std;	//Yeah, yeah, it's just a competition. I'm gonna stick this here.

void MakeTidy(string& s) {

	int breakPoint = -1;
	bool isTidy = true;
	for (int i = 1; i < s.size(); i++) {
		if (s[i] < s[i - 1]) {
			isTidy = false;
			breakPoint = i - 1;
			break;
		}
	}

	if (!isTidy) {
		while (breakPoint > 0 && s[breakPoint - 1] == s[breakPoint])
			breakPoint--;

		s[breakPoint] = s[breakPoint] - 1;
		for (int i = breakPoint + 1; i < s.size(); i++) {
			s[i] = '9';
		}
	}

	if (s[0] == '0') {
		for (int i = 0; i < s.size() - 1; i++) {
			s[i] = s[i + 1];
		}
		s.resize(s.size() - 1);
	}
}

int main()
{
	int testCount;
	cin >> testCount;

	for (int i = 0; i < testCount; i++) {
		string s;
		cin >> s;

		MakeTidy(s);

		cout << "Case #" << i + 1 << ": " << s << endl;
	}

    return 0;
}

