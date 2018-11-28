#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int T, R, C;

map<char, bool> isExpanded;

void solve(vector<string> &grid) {
	char pivot;
	for(int r = 0; r < R; r++) {
		for(int c = 0; c < C; c++) {
			pivot = grid[r][c];
			if(isExpanded[pivot]) { continue; }
			else { isExpanded[pivot] = true; }
			if(pivot != '?') {
				int leftPiv = c, rightPiv = c;
				// Expand left
				for(int x = c-1; x >= 0; x--) {
					if(grid[r][x] == '?') {
						leftPiv = x;
						grid[r][x] = pivot;
					}
					else {
						leftPiv = x+1;
						break; }
				}

				// Expand right
				for(int x = c+1; x < C; x++) {
					if(grid[r][x] == '?') {
						rightPiv = x;
						grid[r][x] = pivot;
					}
					else {
						rightPiv = x-1;
						break; }
				}

				// Expand up
				for(int y = r-1; y >= 0; y--) {
					bool works = true;
					for(int x = leftPiv; x <= rightPiv; x++) {
						if(grid[y][x] != '?') {
							works = false;
							break;
						}
					}
					if(works) {
						for(int x = leftPiv; x <= rightPiv; x++) { grid[y][x] = pivot; }
					} else { break; }
				}

				// Expand down
				//cout << pivot << ":" << leftPiv << ":" << rightPiv << endl;
				for(int y = r+1; y < R; y++) {
					bool works = true;
					for(int x = leftPiv; x <= rightPiv; x++) {
						if(grid[y][x] != '?') {
							works = false;
							break;
						}
					}
					if(works) {
						for(int x = leftPiv; x <= rightPiv; x++) { grid[y][x] = pivot; }
					} else { break; }
				}

				/*for(int t = 0; t < R; t++) {
					cout << grid[t] << endl;
				}*/
			}
		}
	}
	isExpanded.clear();
}

int main() {
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> R >> C;
		vector<string> grid(R);
		for(int r = 0; r < R; r++) {
			cin >> grid[r];
		}

		solve(grid);

		cout << "Case #" << (i+1) << ":" << endl;
		for(int r = 0; r < R; r++) {
			cout << grid[r] << endl;
		}

	}
}
