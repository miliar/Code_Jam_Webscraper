#include <iostream>
#include <fstream>

using namespace std;

bool is_tidy(__int64 n) {
	__int64 d = n / 10;
	__int64 m_old = n % 10;
	//cout << m_old << "\n";

	while (d > 0) {
		__int64 m_new = d % 10;
		//cout << m_new << "\n";

		if (m_new > m_old) {
			return false;
		}
		d = d / 10;
		m_old = m_new;
	}
	return true;
}

int main() {

	ifstream input("B-large.in");
	int t;
	input >> t;

	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		__int64 n;
		input >> n;

		//cout << n << "\n";

		__int64 b = 10;

		while (!is_tidy(n)) {
			n = n - n % b - 1;
			b *= 10;
			//cout << n << "\n";
		}
		cout << n;
		cout << "\n";
	}

	input.close();

	//__int64 n = 999990;

	//cout << is_tidy(n) << "\n";
}