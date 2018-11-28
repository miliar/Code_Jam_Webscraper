#define DEBUG 0
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string grid[25];
bool filled[25];

void solve()
{
	cout << '\n';
	int r, c;
	cin >> r >> c;
	memset(filled, 0, sizeof(filled));
	for (int i = 0; i < r; ++i) {
		cin >> grid[i];
		bool isFirst = true;
		for (int j = 0; j < c; ++j) {
			if (grid[i][j] != '?') {
				filled[i] = true;
				if (isFirst) {
					isFirst = false;
					for (int k = j - 1; k >= 0; --k) {
						grid[i][k] = grid[i][j];
					}
				}
				for (int k = j + 1; k < c && grid[i][k] == '?'; ++k) {
					grid[i][k] = grid[i][j];
				}
			}
		}
	}
	for (int i = 0; i < r; ++i) {
		if (!filled[i]) {
			int ans = -1;
			for (int j = i - 1; j >= 0; --j) {
				if (filled[j]) {
					ans = j;
					for (int k = j; k <= i; ++k) {
						filled[k] = true;
						for (int m = 0; m < c; ++m) {
							grid[k][m] = grid[j][m];
						}
					}
					break;
				}
			}
			if (ans == -1) {
				for (int j = i + 1; j < r; ++j) {
					if (filled[j]) {
						ans = j;
						for (int k = j; k >= i; --k) {
							filled[k] = true;
							for (int m = 0; m < c; ++m) {
								grid[k][m] = grid[j][m];
							}
						}
						break;
					}
				}
			}
		}
	}
	for (int i = 0; i < r; ++i) {
		cout << grid[i] << '\n';
	}
}

int main()
{
	cerr << fixed << setprecision(0);
	cout << fixed << setprecision(20);
	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}
	int _c, _start = static_cast<int>(clock());
	cin >> _c;
	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		cout << "Case #" << _cc << ":";

		solve();

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}
	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;
	return 0;
}
