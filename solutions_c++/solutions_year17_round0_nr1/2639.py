#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tsts = 0; tsts < t; ++tsts) {
		string s;
		int k;
		cin >> s >> k;
		int w = 0;
		for (int i = 0; i < int (s.size()); ++i) {
			if (s[i] != '+') {
				if (i + k > int( s.size())) {
					w = -1;
					break;
				}
				for (int j = 0; j < k; ++j)
					if (s[i+j] == '+')s[i+j] = '-';
					else s[i+j] = '+';
				++w;
			}
		}
		cout << "Case #" << tsts + 1 << ": ";
		if (w == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << w << "\n";

	} 
}