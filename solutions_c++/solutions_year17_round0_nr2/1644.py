#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		string number;
		cin >> number;
		int inv_p = 1;
		while (inv_p < number.size() && number[inv_p - 1] <= number[inv_p]) ++inv_p;
		// Now, inv_p is the first 'untidy' digit
		if (inv_p < number.size()) {
			// Have to fix 
			// 1. -1 from the left side, enforcing the tidyness property
			int c = inv_p - 1;
			--number[c];
			while (c > 0 && number[c - 1] > number[c]) {
				number[c--] = '9';
				--number[c];
			}
			// 2. convert the right side to all-9s
			while (inv_p < number.size()) {
				number[inv_p++] = '9';
			}
		}
        // Output
		cout << "Case #" << casen << ": ";
		// Print w/o leading zeroes
		int i = 0;
		while (number[i] == '0') ++i;
		while (i < number.size()) cout << number[i++];
		cout << '\n';
	}
	return 0;
}

