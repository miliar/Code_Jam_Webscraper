#include <iostream>
#include <string>

using namespace std;

int main() {

	long nbTestCases;
	cin >> nbTestCases;

	for (int x(1) ; x <= nbTestCases ; ++x) {
		string row;
		int k;
		cin >> row >> k;

		bool possible(true);
		size_t l(row.length());
		size_t minMove(0);
		size_t firstSadFace = row.find('-');
		while ( firstSadFace != string::npos) {
			if (firstSadFace + k > l) {
				possible = false;
				break;
			}
			for (int i(0) ; i < k ; ++i) {
				switch (row[firstSadFace+i]) {
				case '+':
					row[firstSadFace+i] = '-';
					break;
				case '-':
					row[firstSadFace+i] = '+';
					break;
				}
			}
			++minMove;
			firstSadFace = row.find('-');
		}

		cout << "Case #" << x << ": ";
		if (!possible) {
			cout << "IMPOSSIBLE";
		} else {
			cout << minMove;
		}
		cout << endl;
	}

	return 0;
}


