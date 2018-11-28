#include<iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		int k;
		cin >> s >> k;
		int num = 0;
		bool possible = true;
		int len = s.length();
		for (int j = 0; j < len; j++) {
			//cout << " Num : " << num << " " << s  << " " << j << " " << k << endl;
			if (s[j] == '-') {
				if (j + k -1 < len) {
					num++;
					for (int a = j; a < j + k; a++) {
						s[a] = (s[a] == '-' ? '+' : '-');
					}
				}
				else {
					possible = false;
					break;
				}
			}
		}
		if (!possible) {
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << (i + 1) << ": " << num << endl;
		}
	}
	return 0;
}