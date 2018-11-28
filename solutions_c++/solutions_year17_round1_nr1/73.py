#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <functional>

using namespace std;
#define lli long long int
const int N = 111;
double M = 1e7;

char f[200][200];
bool used[200][200];

void dprint() {

}

int main() {
	ios_base::sync_with_stdio();
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		cout << endl;
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
			cin >> f[i][j]; used[i][j] = 0;
		}

		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
			if (!used[i][j] && f[i][j] != '?') {
				int left = j - 1, right = j + 1;
				while (left >= 0 && f[i][left] == '?') --left;
				while (right < m && f[i][right] == '?') ++right;
				int top = i - 1, bottom = i + 1;
				while (top >= 0) {
					bool ok = true;
					for (int i1 = left + 1; i1 < right; ++i1) ok &= f[top][i1] == '?';
					if (!ok) break;
					--top;
				}
				while (bottom < n) {
					bool ok = true;
					for (int i1 = left + 1; i1 < right; ++i1) ok &= f[bottom][i1] == '?';
					if (!ok) break;
					++bottom;
				}
				for (int i1 = top + 1; i1 < bottom; ++i1) for (int j1 = left + 1; j1 < right; ++j1) {
					f[i1][j1] = f[i][j];
					used[i1][j1] = true;
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) cout << f[i][j];
			cout << endl;
		}

		//cout << endl;
	}
	return 0;
}
