#include <iostream>
#include <string>

using namespace std;

void main() {
	int tn, n, m;
	cin >> tn;

	for (int t = 1; t <= tn; ++t) {
		string s;
		cin >> s;

		int p = -1;
		for (int i = 0; i < s.length() - 1; ++i) {
			if (s[i] > s[i + 1]) {
				p = i;
				break;
			}
		}

		if (p > -1) {
			int first;
			for (first = p; first >= 0 && s[first] == s[p]; --first) {}
			first++;

			s[first]--;
			
			for (int j = first + 1; j < s.length(); ++j) {
				s[j] = '9';
			}

			while (s[0] == '0') {
				s = s.substr(1);
			}
		}
		
		cout << "Case #" << t << ": " << s << endl;		
	}
}