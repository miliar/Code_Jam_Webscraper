//============================================================================
// Name        : qa-b.cpp
// Author      : Long Pham
//============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	string N;
	string tidy;

	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> N;
		int l = N.length();
		tidy = "";
		int i = 0;
		while (i < l-1 && N[i] <= N[i+1]) {
			i++;
		}

		if (i == l-1) {
			tidy = N;
		} else {
			int j = i;
			while (j > 0 && N[j-1] > N[j] - 1) {
				j--;
			}

			for (int k=0; k < j; k++) {
				tidy += N[k];
			}

			if (j > 0 || N[j] > '1') {
				tidy += N[j] - 1;
			}

			while (j < l-1) {
				j++;
				tidy += '9';
			}
		}

		cout << "Case #" << t+1 << ": " << tidy << endl;
	}
	return 0;
}
