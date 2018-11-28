#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isEmpty(string &x) {
	for(char y : x)
		if(y != '?') return false;
	return true;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int R, C;
		cin >> R >> C;
		vector<string> grid(R);
		for(int r = 0; r < R; r++) {
			cin >> grid[r];
			for(int c = 0; c < C; c++) {
				if(grid[r][c] != '?') {
					int x = c + 1;
					while(x < C and grid[r][x] == '?') {
						grid[r][x] = grid[r][c];
						x++;
					}
					x = c - 1;
					while(x >= 0 and grid[r][x] == '?') {
						grid[r][x] = grid[r][c];
						x--;
					}
				}
			}
		}
		for(int r = 1 ; r < R; r++)
			if(isEmpty(grid[r])) grid[r] = grid[r - 1];
		for(int r = R - 2; r >= 0; r--)
			if(isEmpty(grid[r])) grid[r] = grid[r + 1];
		printf("Case #%d:\n", t);
		for(int r = 0; r < R; r++)
			cout << grid[r] << endl;
	}
}
