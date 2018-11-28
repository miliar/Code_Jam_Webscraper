#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	int t = 0;
	while (++t<=T) {
		string s;
		int k;
		cin >> s >> k;


		int res = 0;
		for (int i = 0; i <= s.length() - k; ++i) {
			if (s[i] == '-') {
				++res;
				for (int j = 0; j < k; ++j) {
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
			}
		}

		for (int i = s.length() - k; i < s.length(); ++i) {
			if (s[i] == '-') {
				res = -1; 
				break;
			}
		}

		cout << "Case #" << t << ": ";
		if(res==-1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}