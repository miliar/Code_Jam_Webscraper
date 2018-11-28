#include <iostream>

using namespace std;

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ti++) {
		string k;
		cin >> k;
		for (int i = k.size() - 1; i > 0; i--) {
			if (k[i -1] > k[i]) {
				k[i - 1]--;
				for (int j = i; j < k.size(); j++) {
					k[j] = '9';
				}
			}
		}
		cout << "Case #" << ti << ": ";
		for (int j = 0; j< k.size(); j++) {
			if (k[j] > '0') {
				cout << k[j];
			}
		}
		cout << endl;
	}
}
