#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int r, c;
		cin >> r >> c;

		vector<string> s(r);
		for (int i = 0; i < r; ++i)
			cin >> s[i];


		for (int i = 0; i < r; ++i) {
			for (int j = 1; j < c; ++j) {
				if (s[i][j] == '?')
					s[i][j] = s[i][j - 1];
			}
			for (int j = c-2; j >=0; --j){
				if (s[i][j] == '?')
					s[i][j] = s[i][j + 1];
			}
		}
		for (int j = 0; j < c; ++j) {
			for (int i = 1; i < r; ++i) {
				if (s[i][j] == '?')
					s[i][j] = s[i-1][j];
			}
			for (int i = r - 2; i >= 0; --i) {
				if (s[i][j] == '?')
					s[i][j] = s[i+1][j];
			}
		}


		cout << "Case #" << t << ": " << endl;
		for (int i = 0; i < r; ++i)
			cout << s[i] << endl;
	}
	return 0;
}