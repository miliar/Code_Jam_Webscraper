#include <iostream>
#include <string>

using namespace std;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
		int count = 0;
		string output = "";

		string S;
		cin >> S;

		size_t length = S.length();
		unsigned* numbers = new unsigned[length];

		for (size_t i = 0; i < length; ++i)
			numbers[i] = (int)S[i] - 48;
		
		bool isTidy = true;
		for (size_t i = 1; i < length; ++i) {
			if (numbers[i] < numbers[i - 1]) {
				isTidy = false;
				break;
			}
		}

		if (isTidy) {
			output = S;
		} else {
			bool flag = false;
			size_t nIndex = 0;
			if (numbers[0] == 1) {
				for (size_t i = 1; i < length; ++i) {
					if (numbers[i] == 1)
						continue;
					else {
						if (numbers[i] == 0)
							flag = true;
						nIndex = i;
						break;
					}
				}
			}

			if (flag) {
				for (size_t i = 0; i < length - 1; ++i)
					output += (char)57; // 9
			} else {
				size_t eIndex = 0;
				for (size_t i = nIndex; i < length; ++i) {
					if (numbers[i] == numbers[nIndex])
						continue;
					else {
						if (numbers[i] > numbers[nIndex])
							nIndex = i;
						else {
							eIndex = i;
							break;
						}
					}
				}

				output = S.substr(0, nIndex);
				output += (char)(48 + numbers[nIndex] - 1);
				for (size_t i = nIndex + 1; i < length; ++i)
					output += (char)57;
			}
		}

		printf("Case #%u: %s\n", caseIndex, output.c_str());
		delete[] numbers;
	}
}
