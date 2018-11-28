#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
using namespace std;

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		string s;
		cin >> s;

		int size = s.size();
		if (size != 1) {
			for (int i = size - 1; i != 0; i--) {
				if (s[i - 1] > s[i]) {
					for (int j = i; j != size; j++) {
						s[j] = '9';
					}
					s[i - 1]--;
				}
			}
		}

		if (s[0] == '0') {
			s = s.substr(1);
		}

		printf("Case #%d: ", t);
		cout << s << endl;
	}

	fclose(stdout);
	return 0;
}