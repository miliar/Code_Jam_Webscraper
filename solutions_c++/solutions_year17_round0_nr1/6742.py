#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ": ";
		int k;
		int count = 0;
		string s;
		cin >> s >> k;
		int i;
		for (i = 0; i < s.length(); i++) {
			if (s[i] == '+') continue;
			count++;
			int j;
			for (j = 0; j < k; j++) {
				if (i+j >= s.length()) break;
				if (s[i+j] == '-') s[i+j] = '+';
				else s[i+j] = '-';
			}
			if (j < k) break;
		}
		if (i < s.length()) cout << "IMPOSSIBLE" << endl;
		else cout << count << endl;
	}
	return 0;
}

