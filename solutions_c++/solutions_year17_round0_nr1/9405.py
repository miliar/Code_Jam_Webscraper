#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		char flip[1001];
		cin >> flip;
		int size;
		cin >> size;

		int length = strlen(flip);
		//cout << "Length :" << length << endl;
		//flip
		int flipTimes = 0;
		for (int j = 0; j < length; ++j) {
			if (flip[j] == '+') {
				continue;
			} else if (flip[j] == '-') {
				if (j + size > length)	{
					//impossible 
					flipTimes = -1;
					break;

				} else {
					flipTimes ++;
					int hasSkipped = 0;
					int skipIndex = 0;
					for (int k = 0; k < size ; ++k) {
						if (flip[j + k] == '-') {
							if (hasSkipped == 0) {
								skipIndex = k;
							}
							flip[j + k] = '+';
						} else {
							hasSkipped = 1;
							flip[j + k] = '-';
						}
					}
					j = j + skipIndex;
				}

			}
		}
		if (flipTimes == -1) {
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << flipTimes << endl;
		}

	}

}