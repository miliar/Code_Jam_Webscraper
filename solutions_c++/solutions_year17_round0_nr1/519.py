#include <string>
#include <iostream>

using namespace std;

void main() {
	size_t testCount;
	cin >> testCount;

	string pan;
	int K;
	for (size_t i = 0; i < testCount; i++) {
		cin >> pan >> K;

		//cout << pan << " " << K << endl;

		size_t flips = 0;
		for (size_t j = 0; j < pan.length()-K+1; j++) {
			if (pan[j] == '-') {
				flips++;
				for (size_t k = j; k < j + K; k++) {
					if (pan[k] == '-') {
						pan[k] = '+';
					} else {
						pan[k] = '-';
					}
				}
			}

			//cout << pan << " " << flips << endl;
		}

		bool allHappy = true;
		for (int i = 0; i < K; i++) {
			if (pan[pan.length()-1-i] == '-') {
				allHappy = false;
				break;
			}
		}

		if (allHappy) {
			cout << "Case #" << i + 1 << ": " << flips << endl;
		} else {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}
	}
}