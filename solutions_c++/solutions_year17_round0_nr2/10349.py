#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

bool tidy(string x) {
	for (int i = 0; i < x.size() - 1; i++) {
		if (x[i] <= x[i + 1]) {
			continue;
		}
		else {
			return false;
		}
	}
	return true;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string input;
		cin >> input;
		unsigned long long count = stoull(input);

		unsigned long long input_int = stoull(input);
		while (count--) {
			if (input_int < 10) {	//10이하는 tidy
				cout << "Case #" << i + 1 << ": " << input << endl;
				break;
			}
			else {					//오름차순이면 tidy
				if (tidy(input)) {
					cout << "Case #" << i + 1 << ": " << input << endl;
					break;
				}
			}
			input_int--;
			input = to_string(input_int);
		}
	}

	return 0;
}