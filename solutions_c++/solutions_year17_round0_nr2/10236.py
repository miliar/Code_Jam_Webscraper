#include <iostream>
#include <string>
#include <list>
using namespace std;

bool isTidy(int n) {
	int nlenght = 1;
	list<int> digits;
	for (int i = 0; i < nlenght; i++) {
		int digit = n % 10;
		digits.push_back(digit);
		n /= 10;
		if (n >= 1)
			nlenght++;
		else break;
	}

	digits.reverse();
	list<int> sortedList = digits;
	sortedList.sort();

	if (sortedList == digits)
		return true;

	return false;
}

void main() {
	int t, n;
	cin >> t;  //num test cases
	for (int i = 1; i <= t; i++) {
		cin >> n;
		bool tidyFound = false;

		while (!tidyFound) {
			tidyFound = isTidy(n);

			if (tidyFound)
				break;
			else
				n -= 1;
		}

		cout << "Case #" << i << ": " << n << endl;
		
	}
}	