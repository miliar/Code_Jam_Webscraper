#include <iostream>
#include <string>
using namespace std;

int main() {

	int T;
	cin >> T;

	for (int tt = 1; tt <= T; tt++) {

		int R, C;
		cin >> R >> C;
		string arr[50];

		for (int i = 0; i < R; i++) {
			cin >> arr[i];
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {

				if (arr[i][j] != '?') {

					int k = j - 1;
					while (k >= 0 && arr[i][k] == '?') {
						arr[i][k] = arr[i][j];
						k--;
					}
					k = j + 1;
					while (k < C && arr[i][k] == '?') {
						arr[i][k] = arr[i][j];
						k++;
					}
				}
			}
		}

		for (int i = 1; i < R; i++) {
			bool chk = false;
			for (int j = 0; j < C; j++) {
				if (arr[i][j] != '?') chk = true;
			}
			if (!chk) {
				for (int j = 0; j < C; j++) {
					arr[i][j] = arr[i - 1][j];
				}
			}
		}

		for (int i = R - 2; i >= 0; i--) {
			bool chk = false;
			for (int j = 0; j < C; j++) {
				if (arr[i][j] != '?') chk = true;
			}
			if (!chk) {
				for (int j = 0; j < C; j++) {
					arr[i][j] = arr[i + 1][j];
				}
			}
		}

		cout << "Case #" << tt << ":" << endl;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cout << arr[i][j];
			}
			cout << endl;
		}
	}
}