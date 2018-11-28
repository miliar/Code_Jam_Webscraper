#include <iostream>
#include <string>

using namespace std;

string a;

int main() {
	int T;
	cin >> T;
	for (int k = 1; k <= T; k++) {
		cin >> a;
		cout << "Case #" << k << ": ";
		bool flag = true;
		int pos;
		for (pos = 1; pos < a.length(); pos++) {
			if (a[pos] < a[pos - 1]) {
				flag = false;
				break;
			}
		}
		pos--;
		if (!flag) {
			for (; pos >= 0; pos--) {
				a[pos]--;
				if (pos == 0 || a[pos] >= a[pos - 1]) break;
			}
		}
		for (int i = 0; i <= pos; i++) {
			if (a[i] != '0')
				cout << a[i];
		}
		for (int i = pos + 1; i < a.length(); i++)
			cout << "9";
		cout << endl;
	}

	return 0;
}
