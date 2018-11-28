#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAX = 100 + 5;
char grid[MAX][MAX];
int r, c;
vector<int> pos[1000 + 5];

int main() {
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	int kase = 1;
	while(t--) {
		cin >> r >> c;
		fori(i, 1, c + 1) {
			pos[i].clear();
		}
		fori(i, 1, r + 1) {
			fori(j, 1, c + 1) {
				cin >> grid[i][j];
				if(grid[i][j] != '?') {
					pos[j].push_back(i);
				}
			}
		}
		int limit_col = 1;
		fori(i, 1, c + 1) {
			if(!pos[i].empty()) {
				fori(k, 0, pos[i].size()) {
					int each = pos[i][k];
					char letter = grid[each][i];
					int row_start = (k == 0) ? 1 : each; 
					int row_end = (k == (int) pos[i].size() - 1) ? r : pos[i][k + 1] - 1;
					fori(row, row_start, row_end + 1) {
						fori(col, limit_col, i + 1) {
							grid[row][col] = letter;
						}
					}
				}
				limit_col = i + 1;
			}
		}
		if(limit_col <= c) {
			ford(i, c, 1) {
				if(!pos[i].empty()) {
					fori(k, 0, pos[i].size()) {
						int each = pos[i][k];
						char letter = grid[each][i];
						int row_start = (k == 0) ? 1 : each; 
						int row_end = (k == (int) pos[i].size() - 1) ? r : pos[i][k + 1] - 1;
						fori(row, row_start, row_end + 1) {
							fori(col, i + 1, c + 1) {
								grid[row][col] = letter;
							}
						}
					}
					break;
				}
			}
		}
		cout << "Case #" << kase++ << ":" << '\n';
		fori(i, 1, r + 1) {
			fori(j, 1, c + 1) {
				cout << grid[i][j];
			}
			cout << '\n';
		}
	}

	return 0;
}

