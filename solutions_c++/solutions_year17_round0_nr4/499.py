#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

using ll = long long;
ll const INF = 1000000000;

int main(void) {

	ios::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	ll T;
	cin >> T;

	for (ll test = 1; test <= T; test++) {

		bool col[101], row[101];
		bool dia1[201];
		bool dia2[201];
		char GridOriginal[101][101];
		bool GridPlus[101][101], GridCross[101][101];


		// Clear all arrays
		for (int i=0;i<101;i++){
			for (int j = 0; j < 101; j++) {
				GridPlus[i][j] = false;
				GridCross[i][j] = false;
				GridOriginal[i][j] = '.';
			}
		}
		for (int i = 0; i < 101; i++) {
			col[i] = false;
			row[i] = false;
		}
		for (int i = 0; i < 201; i++) {
			dia1[i] = false;
			dia2[i] = false;
		}
		// End of clearing arrays

		int N, M;
		cin >> N >> M;

		for (int i = 0; i < M; i++) {
			char in; int r, c; cin >> in >> r >> c; r--; c--;
			GridOriginal[r][c] = in;
			if (in == '+' || in == 'o') {
				GridPlus[r][c] = true;
				dia1[r + c] = true;
				dia2[r - c + 100] = true;
			}
			if (in == 'x' || in == 'o') {
				GridCross[r][c] = true;
				col[c] = true;
				row[r] = true;
			}
		}


		// Place out the crosses
		for (int r = 0; r < N; r++) {
			if (row[r]) continue;
			for (int c = 0; c < N; c++) {
				if (!col[c]) {
					col[c] = true;
					GridCross[r][c] = true;
					break;
				}
			}
		}


		for (int r = 0; r < N; r++){
			if (!dia1[r] && !dia2[r + 100]) {
				dia1[r] = true;
				dia2[r + 100] = true;
				GridPlus[r][0] = true;
			}
		}

		for (int r = 0; r < N; r++) {
			if (!dia1[r + N - 1] && !dia2[r + 100 - N + 1]) {
				dia1[r + N - 1] = true;
				dia2[r + 100 - N + 1] = true;
				GridPlus[r][N-1] = true;
			}
		}

		for (int c = 0; c < N; c++) {
			if (!dia1[c] && !dia2[ - c + 100]) {
				dia1[c] = true;
				dia2[- c + 100] = true;
				GridPlus[0][c] = true;
			}
		}

		for (int c = 0; c < N; c++) {
			if (!dia1[N - 1 + c] && !dia2[N - 1 - c + 100]) {
				dia1[N - 1 + c] = true;
				dia2[N - 1 - c + 100] = true;
				GridPlus[N - 1][c] = true;
			}
		}

		int ans = 0, changes=0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (GridCross[r][c]) ans++;
				if (GridPlus[r][c]) ans++;
				if (GridOriginal[r][c] == 'o') {
					continue;
				}
				if (GridCross[r][c] && GridPlus[r][c]) {
					changes++;
					continue;
				}
				if (GridOriginal[r][c] != '.') {
					continue;
				}
				if (GridCross[r][c] || GridPlus[r][c]) {
					changes++;
				}
			}
		}

		cout << "Case #" << test << ": " << ans << " " << changes << "\n";

		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (GridOriginal[r][c] == 'o') {
					continue;
				}
				if (GridCross[r][c] && GridPlus[r][c]) {
					cout << "o " << r+1 << " " << c+1 << "\n";
					continue;
				}
				if (GridOriginal[r][c] != '.') {
					continue;
				}
				if (GridCross[r][c]) {
					cout << "x " << r+1 << " " << c+1 << "\n";
				}
				if (GridPlus[r][c]) {
					cout << "+ " << r + 1 << " " << c+1 << "\n";
				}
			}
		}
		
	}

	return 0;
}