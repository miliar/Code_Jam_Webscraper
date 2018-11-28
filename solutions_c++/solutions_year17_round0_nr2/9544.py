#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
using namespace std;
int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t  = 0;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		long long n;
		cin >> n;

		int answer = 0;
		for (int i = n; i > 0; i--) {
			string number = to_string(i);
			// cout << number << endl;
			bool is_increasing = true;
			for (int j = 0; j < number.size() - 1; j++) {
				// cout << number[j] << " " << number[j+1] << endl;
				if (number[j] > number[j+1]) {
					is_increasing = false;
					break;
				}
			}

			if (is_increasing || i < 10) {
				answer = i;
				break;
			}
		}

		cout << "Case #" << test << ": " << answer << endl;
	}



	return 0;
}