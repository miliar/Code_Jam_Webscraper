#include <iostream>
#include <string>

using namespace std;
int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1<< ": ";

		string number;
		cin >> number;

		bool flip = false;
		
		for (int start = number.size() - 1; start >= 0; start--) {
			for (int j = start; j < number.size() - 1; j++) {
				if (number[j] > number[j+1]) {
					number[j]--;
					for (int jj = j+1; jj < number.size(); jj++) {
						number[jj] = '9';
					}
				}
			}
		}

		for (int j = 0; j < number.size(); j++) {
			if (number[j] == '0') {
				number.erase(number.begin() + j);
			}
		}
		cout << number << endl;
	}
}

