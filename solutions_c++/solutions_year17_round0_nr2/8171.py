#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;

	for(int tc = 1 ; tc <= t ; tc++){
		string x, y; cin >> x;

		for (int i = 0; i < x.length() - 1; i++) {
			if (x[i] > x[i + 1]) {
				int j;
				for (j = i; j >= 1; j--)
					if (x[j] != x[j - 1]) break;

				x[j]--;

				for (j = j + 1; j < x.length(); j++) x[j] = '9';
				break;
			}
		}

		cout << "Case #" << tc << ": ";

		int fg = 0;

		for (int i = 0; i < x.length(); i++) {
			if (x[i] != '0') fg = 1;
			if (fg == 1) cout << x[i];
		}cout << endl;
	}

}