#include <iostream>

using namespace std;

int ds[20];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string N;
		cin >> N;
		for (int i = 0; i < N.size(); i++) {
			ds[i] = N[i] - '0';
		}

		for (int k = 0; k < 20; k++) {
			for (int i = N.size() - 1; i > 0; i--) {
				if (ds[i] < ds[i - 1]) {
					for (int k = i; k < N.size(); k++) ds[k] = 9;
					int j = i - 1;
					while (j > 0 && ds[j] == 0) {
						ds[j] = 9;
						j--;
					}
					ds[j]--;
				}
			}
		}

		cout << "Case #" << t << ": ";
		int i = 0;
		while (ds[i] == 0) i++;
		for (int j = i; j < N.size(); j++) {
			cout << ds[j];
		}
		cout << endl;
	}

	return 0;
}