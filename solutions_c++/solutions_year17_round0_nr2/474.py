#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t; cin >> t;

	for (int j=1; j<=t; ++j) {
		string s; cin >> s;

		int i=0;
		while (i+1<s.size() && s[i] <= s[i+1]) ++i;


		if (i == s.size()-1) {
			cout << "Case #" << j << ": " << s << endl;
			continue;
		}

		--s[i];

		while (i > 0 && s[i] < s[i-1]) {
			--s[--i];
		}

		++i;

		for (; i<s.size(); ++i) {
			s[i] = '9'	;
		}

		int begin=0;
		while (s[begin] == '0') ++begin;

		cout << "Case #" << j << ": " << s.substr(begin) << endl;
	}
}
