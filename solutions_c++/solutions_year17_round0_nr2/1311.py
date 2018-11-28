#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		string n;
		cin >> n;
		for (int i = n.size() - 1; i > 0; i--) {
			if (n[i - 1] > n[i]) {
				n[i - 1]--;
				for (int j = i; j < n.size(); j++) {
					n[j] = '9';
				}
			}
		}
		if (n[0] == '0') n = n.substr(1);
		cout << "Case #" << test << ": ";
		cout << n;
		cout << endl;
	}
}