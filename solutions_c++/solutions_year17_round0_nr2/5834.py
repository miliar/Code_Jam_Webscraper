#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		string maxNum;
		cin >> maxNum;

		string maxTidy = maxNum;

		for (int i = 1; i < maxNum.length(); i++) {
			if (maxNum.at(i) < maxNum.at(i-1)) {
				if (i == 1) {
					if (maxNum.at(0) != '1') {
						maxTidy = string(1, maxNum.at(0) - 1);
					} else {
						maxTidy = "";
					}
					maxTidy.append(maxNum.length() - i, '9');
				} else {
					int start = i - 1;
					while (start > 0 && maxNum.at(start) == maxNum.at(start - 1)) {
						start--;
					}
					if (start > 0) {
						maxTidy = maxNum.substr(0, start);
						maxTidy += string(1, maxNum.at(start) - 1);
						maxTidy.append(maxNum.length() - start - 1, '9');
					} else {
						if (maxNum.at(0) != '1') {
							maxTidy = string(1, maxNum.at(0) - 1);
						} else {
							maxTidy = "";
						}
						maxTidy.append(maxNum.length() - 1, '9');
					}
				}
				break;
			}
		}

		cout << "Case #" << caseNum << ": " << maxTidy << endl;

	}
	return 0;
}


