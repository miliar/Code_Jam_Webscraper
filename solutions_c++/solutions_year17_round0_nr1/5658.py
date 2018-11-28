#include <iostream>
#include <string>

using namespace std;

int main() {

	int testcase;
	cin >> testcase;

	for (int i = 1; i <= testcase; i++) {

		bool impossible = false;
		string series;
		int windowsize;
		cin >> series;
		cin >> windowsize;
		int flip = 0;

		int len = series.length();
		for (int j = 0; j < len; j++) {
			if (series[j] == '-') {
				if (j > len - windowsize) {
					impossible = true;
					break;
				}
				else {
					flip++;
					for (int k = j; k < j + windowsize; k++) {
						if (series[k] == '-') {
							series[k] = '+';
						}
						else {
							series[k] = '-';
						}
					}
				}
			}
		}

		if (impossible) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i << ": " << flip << endl;
		}

	}



}