#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++) {
		string input;
		int flipper;
		cin >> input >> flipper;
		string current = input;
		int moves = 0;
		int length = input.length();
		for(int i = 0; i < length - flipper + 1; i++) {
			if(current[i] == '-') {
				moves++;
				for(int j = i; j < i + flipper; j++) {
					if(current[j] == '+') {
						current[j] = '-';
					} else {
						current[j] = '+';
					}
				}
			}
		}

		int is_ok = 1;
		for(int i = 0; i < length; i++) {
			if(current[i] == '-') {
				is_ok = 0;
			}
		}
		if(is_ok == 0) {
			cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << z << ": " << moves << endl;
		}
	}
}