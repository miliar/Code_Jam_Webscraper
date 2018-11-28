#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	
	int n, c;
	bool lul;
	string input_string, res;
	
	for (int q = 0; q < t; q++) {
		cin >> input_string;
		n = input_string.size();
		c = 0;
		
		lul = false;
		
		for (int i = 1; i < n; i++) {
			if (input_string[i] < input_string[i - 1]) {
				lul = true;
				break;
			}
			
			if (input_string[i] > input_string[i - 1]) {
				c = i;
			}
		}
		
		cout << "Case #" << q + 1 << ": ";
		if (!lul) {
			cout << input_string;
		} else {
			for (int i = 0; i < c; i++) {
				cout << input_string[i];
			}
			if (input_string[c] != '1') {
				cout << (char)((int)input_string[c] - 1);
			}
			for (int i = c + 1; i < n; i++) {
				cout << "9";
			}
		}
		cout << endl;
	}
}