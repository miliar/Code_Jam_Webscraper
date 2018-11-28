#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int R, C;
		cin >> R >> C;
		vector<string> g(R);
		for (int r = 0; r < R; r++){
			cin >> g[r];
		}

		set<char> checked;
		for (int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				if (g[r][c] == '?'){
					continue;
				}
				if (!checked.insert(g[r][c]).second) {
					continue;
				}

				int imin = c, imax = c;
				for (int i = c-1; i >= 0; i--){
					if (g[r][i] == '?') {
						g[r][i] = g[r][c];
						imin = i;
					}
					else {
						break;
					}
				}
				for (int i = c+1; i < C; i++){
					if (g[r][i] == '?') {
						g[r][i] = g[r][c];
						imax = i;
					}
					else {
						break;
					}
				}

				for (int i = r + 1; i < R; i++) {
					bool ok = true;
					for (int j = imin; j <= imax; j++) {
						if (g[i][j] != '?') {
							ok = false;
							break;
						}
					}
					if (ok) {
						for (int j = imin; j <= imax; j++) {
							g[i][j] = g[r][c];
						}
					}
					else {
						break;
					}
				}
			}
		}

		for (int r = R - 2; r >= 0; r--) {
			if (g[r][0] == '?') {
				g[r] = g[r + 1];
			}
		}
		printf("Case #%d:\n", t + 1);
		for (int i = 0; i < R; i++) {
			cout << g[i] << endl;
		}
	}
}	