#include <iostream>
#include <string>
using namespace std;

void tidyNumbers(string& s) {
	int decreasePos = (int)s.size();
	for (int i = (int)s.size() - 2; i >= 0; --i) {
		if (s[i] > s[i + 1]) {
			decreasePos = i;
			s[i]--;
		}
	}
	for (int i = decreasePos + 1; i < (int)s.size(); ++i)
		s[i] = '9';
	while (s[0] == '0')
		s.erase(0, 1);
}

int main() {
	int testCount;
	string test;
	cin >> testCount;
	for (int i = 1; i <= testCount; ++i) {
		cin >> test;
		tidyNumbers(test);
		cout << "Case #" << i << ": " << test << endl;
	}
	return 0;
}
