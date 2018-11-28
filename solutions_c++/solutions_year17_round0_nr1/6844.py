#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {

	ifstream input("A-large.in");

	int t = 0;
	input >> t;

	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		string x;
		input >> x;

		int pan_size = 0;
		input >> pan_size;

		int start = 0;
		int end = x.length() - 1;

		int count = 0;
		bool happy = false;

		while (true) {
			while ((x[start] == '+') && (start <= end)) {
				if (start == end) {
					happy = true;
				}
				start++;
			}

			if (happy) {
				break;
			}

			if (start + pan_size - 1 <= end) {
				for (int j = start; j <= start + pan_size - 1; j++) {
					if (x[j] == '-') {
						x[j] = '+';
					}
					else {
						x[j] = '-';
					}
				}
				count++;
			}
			else {
				break;
			}


		}

		if (happy) {
			cout << count;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << "\n";
	}


	input.close();
}