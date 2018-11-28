#include <iostream>
#include <string>
using namespace std;

int main (void) {
	int t; cin >> t;
	for (int y = 1; y <= t; y++) {
		string s; cin >> s;
		int k; cin >> k;
		int c = 0;
		int flag = 0;
		for (int i = 0; i < s.size()-k+1; i++) {
			if (s[i] == '+')
				continue;
			else {
				for (int j = i; j < i + k; j++) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
				c++;
			}
		}
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				flag = 1;
				break;
			}

		}
		if (flag == 1)
			cout << "Case #" << y << ": "<< "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << y << ": " << c << endl;

	}

	return 0;
}