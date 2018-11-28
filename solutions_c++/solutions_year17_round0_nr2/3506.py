#include <bits/stdc++.h>
using namespace::std;

int main() {
	int t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		int prev = 0;
		string s;
		cin >> s;
		for (int i = 1; i < s.size(); i++) {
			if (s[i] < s[i - 1]) {
				for (i = prev + 1; i < s.size(); i++)
					s[i] = '9';
				if (s[prev] == '1')
					s.erase(prev, 1);
				else
					s[prev]--;
			} else if (s[i] > s[i - 1])
				prev = i;
		}
		cout << "Case #" << caseno << ": " << s << endl;
	}
	return 0;
}