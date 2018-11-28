#include <iostream>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	int k;
	string s;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> s >> k;
		cout << "Case #" << tcount << ": ";

		int count = 0;
		//char state = '+';
		//int minusCount = k;

		for (int i = 0; i < s.length() - k + 1; ++i) {
			if (s[i] != '+') {
				++count;
				for (int j = 0; j < k; ++j)
					s[i + j] = '-' + '+' - s[i + j];
			}
		}
		for (int i = s.length() - k + 1; i < s.length(); ++i) {
			if (s[i] != '+')
				goto impossible;
		}

		cout << count << endl;
		continue;
		
	impossible:
		cout << "IMPOSSIBLE\n";
	}

	return 0;
}