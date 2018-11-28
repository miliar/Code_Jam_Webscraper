#include <iostream>
#include <string>
using namespace std;

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++) {
		int n;
		string str;
		cin >> str;
		
		for (int i = str.size() - 1; i; i--) {
			if (str[i] < str[i - 1]) {
				for (int j = i - 1;; i--) {
					str[j]--;
					if (str[j] < '0') str[j] = '9';
					else break;
				}
				for (int j = i; j < str.size(); j++) {
					str[j] = '9';
				}
			}
		}
		if (str[0] == '0') str.erase(str.begin());
		cout << "Case #" << t << ": " << str << endl;
	}

	return 0;
}