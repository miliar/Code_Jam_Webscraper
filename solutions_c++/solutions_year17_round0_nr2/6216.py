#include <iostream>
#include <string>

using namespace std;

int main() {

	long nbTestCases;
	cin >> nbTestCases;

	for (int x(1) ; x <= nbTestCases ; ++x) {
		string n;
		cin >> n;
		size_t l(n.length());
		if (l > 1) {
			size_t pos(1);
			while (pos < l) {
				char digit = n[pos];
				char prevDigit = n[pos-1];
				if (digit < prevDigit) {
					// make previous lower and make all next 9
					--n[pos-1];
					for (size_t i(pos) ; i < l ; ++i) {
						n[i] = '9';
					}
					--pos;
					if (pos == 0) {
						++pos;
					}
				} else {
					++pos;
				}
			}
		}

		size_t pos = n.find_first_not_of('0');
		cout << "Case #" << x << ": " << n.substr(pos) << "\n";
	}
	cout << flush;

	return 0;
}


