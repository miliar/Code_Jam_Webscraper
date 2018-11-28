#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;
typedef long long ll;
typedef vector<int> VI;

int n, m;
string firstcol;
void solvebig(int circ_col, int plus_f, int circ_f) {
	cout << 3*n-2 << " " << 3*n-3-plus_f-circ_f+(firstcol[circ_col] == '+' ? 1 : 0) << '\n';
	for (int j = 1; j <= n; ++j) {
		char c = (j == circ_col ? 'o' : '+');
		if (c != firstcol[j])
			cout << c << " 1 " << j << '\n';
	}
	for (int j = 2; j < n; ++j) {
		cout << "+ " << n << " " << j << '\n';
	}
	if (circ_col != 1) cout << "x " << n << " " << 1 << '\n';
	else cout << "x " << n << " " << n << '\n';
	for (int k = 2; k < n; ++k) {
		if (k != circ_col)
			cout << "x " << k << " " << k << '\n';
	}
	if (circ_col != 1 && circ_col != n) {
		cout << "x " << circ_col << " " << n << '\n';
	}
}
int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		cin >> n >> m;
		firstcol = string(n+1, '.');
		int circ_col = 1;
		int plus_f = 0;
		int circ_f = 0;
		for (int k = 0, i, j; k < m; ++k) {
			char c;
			cin >> c >> i >> j;
			if (c != '+') circ_col = j;
			if (i > 1) continue;
			if (c == '+') firstcol[j] = '+';
			if (c == 'o') firstcol[j] = 'o';
			if (c == '+') ++plus_f;
			if (c == 'o') ++circ_f;
		}
		if (n > 1) solvebig(circ_col, plus_f, circ_f);
		else {
			if (firstcol[1] != 'o') {
				cout << "2 1\n";
				cout << "o 1 1\n";
			} else {
				cout << "2 0\n";
			}
		}
	}
}