#include <iostream>
#include <string>

using namespace std;

void printTidyNumber(const string& s) {
	int sLen = s.length();
	char prev = s[sLen-1];
	int maxSwitch = 0;
	for (int i = sLen-2, j = 1; i >= 0; i--, j++)
	{
		if (s[i] > prev) {
			prev = s[i] - 1;
			maxSwitch = j;
		}
		else
		{
			prev = s[i];
		}
	}
	if (maxSwitch == 0)
		cout << s;
	else
	{
		for (int i = 0; i < sLen - 1 - maxSwitch; i++)
			cout << s[i];
		if (s[sLen - 1 - maxSwitch] != '1')
			cout << (char)(s[sLen - 1 - maxSwitch] - 1);
		for (int i = 0; i < maxSwitch; i++)
			cout << '9';
	}
}

int main() {
	int T;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		string s;
		cin >> s;
		cout << "Case #" << iCase << ": ";
		printTidyNumber(s);
		cout << endl;
	}
}
