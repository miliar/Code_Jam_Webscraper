#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	string str;
	bool f = false;
	cin >> n;
	for (int i = 0;i < n; ++i) {
		cin >> str;
		f = false;
		for (int j = 0;j < str.size() - 1; ++j) {
			if ( str[j] > str[j + 1]) {
				if (str[j + 1] == '0' && str[j] == '1') {
					f = true;
					cout << "Case #" << i + 1 << ": ";
					for (int k = 0;k < str.size() - 1; ++k) cout << "9";
					cout << "\n";
					break;
				} else {
					int l;
					str[j]--;
					for (int z = j; z >= 0; --z) {
						if (str[z] < str[z - 1]) str[z - 1] = str[z];
						else {
							l = z;
							break;
						}
					}
					f = true;
					for (int k = l + 1;k < str.size();++k) str[k] = '9';
					cout << "Case #" << i + 1 << ": ";
					for (int k = 0;k < str.size(); ++k) cout << str[k];
					cout << "\n";
					break;
				}
			}	
		}
		if (!f) {
			cout << "Case #" << i + 1 << ": ";
			for (int k = 0;k < str.size(); ++k) cout << str[k];
			cout << "\n";
		}
	}	
	return 0;
}
