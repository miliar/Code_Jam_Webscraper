#include <iostream>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	string s;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> s;
		cout << "Case #" << tcount << ": ";

		int pt = -1;
		for (int i = 1; i < s.length(); ++i) {
			if (s[i] < s[i - 1]) {
				pt = i - 1;
				break;
			}
		}

		if (pt == -1) {
			cout << s << endl;
			continue;
		}
		while (pt > 0) {
			if (s[pt - 1] == s[pt])
				--pt;
			else
				break;
		}
		s[pt] = s[pt] - 1;
		for (int i = pt + 1; i < s.length(); ++i)
			s[i] = '9';
		if (s[0] == '0')
			s = s.substr(1);

		cout << s << endl;
		continue;
	}

	return 0;
}