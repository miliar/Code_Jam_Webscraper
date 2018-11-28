#include <iostream>
#include <fstream>
#include <stdio.h>

#include <string>
#include <map>


using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i0 = 1; i0 <= t; ++i0) {
		cout << "Case #" << i0 << ": ";

		string s;
		cin >> s;

		if (s.size() == 1) cout << s << endl;
		else {
			int first = -1;
			for (int i = 1; i < s.size(); ++i) {
				if (s[i] < s[i-1]) {
					first = i;
					break;
				}
			};
			if (first == -1) {
				cout << s << endl;
				continue;
			};

			for (int i = first; i < s.size(); ++i)
				s[i] = '9';

			int i = first-1;

			while (i >= 0) {
				s[i] = s[i]-1;
				if (i == 0 || s[i-1] <= s[i]) break;
				s[i] = '9';
				i--;
			};

			if (s[0] == '0') {
				string t;
				for (int i = 0; i < s.size()-1;++i)
					t.push_back('9');
				cout << t << endl;
				continue;
			}

			cout << s << endl;

		};

	};

}