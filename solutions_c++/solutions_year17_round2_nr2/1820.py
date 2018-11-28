#include<iostream>
#include<string>
using namespace std;

char itocol(int num) {
	switch (num) {
	case 0: return 'R';
	case 1: return 'O';
	case 2: return 'Y';
	case 3: return 'G';
	case 4: return 'B';
	case 5: return 'V';
	default: return '-';
	}
}

int main() {
	int T = 0;
	cin >> T;
	string output[100];
	for (int k = 0; k < T; k++) {
		string out;
		bool imp = false;
		int N = 0;
		int col[6];
		int largest = 0;
		int antil = 0;
		cin >> N;
		for (int i = 0; i < 6; i++) {
			cin >> col[i];
			if (col[i] > col[largest])
				largest = i;
		}
		for (int i = 0; i < 6; i++) {
			if (i != largest) {
				antil += col[i];
			}
		}

		if (antil < col[largest]) {
			output[k] = "IMPOSSIBLE";
		}
		else {

			for (int j = 0; j < N; j++) {
				int L = 0;
				if (largest == 0)
					L = 1;

				for (int i = 0; i < 6; i++) {
					if (i != largest) {
						if (col[i] >= col[L]) 
							L = i;
					}
				}

				if (col[L] != 0) {

					if (col[largest] != 0) {
						output[k] += itocol(largest);
						col[largest]--;
					}
					output[k] += itocol(L);
					col[L]--;
				}

			}

		}
	}

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": " << output[i] << "\n";
	}

	while(1){}
	return 0;
}