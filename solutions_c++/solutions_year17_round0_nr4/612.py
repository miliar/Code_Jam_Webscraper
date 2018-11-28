#include <bits\stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
	int t; cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		int n, m; cin >> n >> m;
		vector<vector<char>> board(n, vector<char>(n, '.'));
		int anyX = 0, anyO = 0;
		for (int i = 0; i < m; ++i) {
			char s; int r, c;
			cin >> s >> r >> c; r--; c--;
			//assert(r == 0);
			board[r][c] = s;
			anyX += (s == 'x');
			anyO += (s == 'o');
		}
		if (n == 1) {
			cout << "Case #" << ti << ": " << 2 << " " << (anyO ? 0 : 1) << endl;
			if (!anyO) cout << "o 1 1" << endl;
			continue;
		}
		vector<string> res;
		for (int i = 0; i < n; ++i) {
			char ch = (board[0][i] == 'x' || board[0][i] == 'o' || (i == 0 && (!anyX && !anyO)) ? 'o' : '+');
			if (board[0][i] != ch) {
				board[0][i] = ch;
				res.push_back(string(1, board[0][i]) + " 1 " + to_string(i + 1));
			}
		}
		if (board[0][n - 1] != 'o') {
			int r = 2;
			for (int i = 0; i < n; ++i) {
				if (board[0][i] == 'x' || board[0][i] == 'o') continue;
				res.push_back("x " + to_string(r++) + " " + to_string(i + 1));
			}
		}
		else {
			for (int i = 0; i < n - 1; ++i) {
				if (board[0][i] == 'x' || board[0][i] == 'o') continue;
				res.push_back("x " + to_string(i + 2) + " " + to_string(n - 1 - i));
			}
		}
		for (int i = 1; i < n-1; ++i) {
			res.push_back("+ " + to_string(n) + " " + to_string(i + 1));
		}
		cout << "Case #" << ti << ": " << (3 * n - 2) << " " << res.size() << endl;
		for (int i = 0; i < res.size(); ++i) {
			cout << res[i] << endl;
		}
	}
}