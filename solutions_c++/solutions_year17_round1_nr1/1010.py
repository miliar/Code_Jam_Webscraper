#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int ti = 1; ti <= t; ti++) {
		int r;
		int c;
		cin >> r >> c;

		vector<string> cake(r);

		for (int i = 0; i < r; i++) {
			cin >> cake[i];
		}

		for (int i = 0; i < r; i++) {
			for (int j = 1; j < c; j++) {
				if (cake[i][j-1] != '?' && cake[i][j] == '?') {
					cake[i][j] = cake[i][j-1];
				}
			}

			for (int j = c - 2; j >= 0; j--) {
				if (cake[i][j+1] != '?' && cake[i][j] == '?') {
					cake[i][j] = cake[i][j+1];
				}
			}
		}

		for (int j = 0; j < c; j++) {
			for (int i = 1; i < r; i++) {
				if (cake[i-1][j] != '?' && cake[i][j] == '?') {
					cake[i][j] = cake[i-1][j];
				}
			}

			for (int i = r - 2; i >= 0; i--) {
				if (cake[i+1][j] != '?' && cake[i][j] == '?') {
					cake[i][j] = cake[i+1][j];
				}
			}
		}

		cout << "Case #" << ti << ":" << endl;

		for (auto& item : cake) {
			cout << item << endl;
		}
	}
}
