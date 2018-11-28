#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int testcase;
	cin >> testcase;
	for (int t = 1; t <= testcase; t++) {
		string s;
		cin >> s;
		int k, count = 0, flag = 0;
		cin >> k;
		for (int i = 0; i < s.length() - k + 1; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i + k; j++) {
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				count++;
			}
		}
		for (int i = s.length() - k + 1; i < s.length(); i++) {
			if (s[i] == '-')
				flag = 1;
		}
		cout << "Case #" << t << ": ";
		if (flag == 1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << count << endl;
	}
	return 0;
}