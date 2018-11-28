#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

bool a[1100];

int main() {
	int T, k;
	string input;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int cnt = 0;
		bool success = true;
		cin >> input >> k;
		for (int j = 0; j < input.length(); j++) {
			a[j] = input[j] == '+';
		}
		for (int j = 0; j <= input.length() - k; j++) {
			if (a[j] == false) {
				for (int l = 0; l < k; l++) {
					a[j + l] = !a[j + l];
				}
				cnt++;
			}
		}
		for (int j = 0; j < input.length(); j++) {
			if (a[j] == false) {
				success = false;
				break;				
			}
		}
		if (success) {
			cout << "Case #" << i + 1 << ": " << cnt << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}
	}
}