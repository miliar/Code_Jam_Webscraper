#include <bits/stdc++.h>
using namespace std;

int N;
char origGrid[105][105];
char grid[105][105];

void dispGrid() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << grid[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

bool inRange(int x, int y) {
	return (1 <= x && x <= N && 1 <= y && y <= N);
}

bool canPlace(char c, int x, int y) {
	if (c == 'x') {
		
		for (int i = 1; i <= N; i++) {
			if (i == x) continue;
			if (grid[i][y] == 'x' || grid[i][y] == 'o') {
				return false;
			}
		}
		for (int j = 1; j <= N; j++) {
			if (j == y) continue;
			if (grid[x][j] == 'x' || grid[x][j] == 'o') {
				return false;
			}
		}
		return true;
		
	} else if (c == '+') {
		
		for (int k = -N; k <= N; k++) {
			if (k == 0) continue;
			int x1 = x + k;
			int y1 = y + k;
			if (inRange(x1, y1) && (grid[x1][y1] == '+' || grid[x1][y1] == 'o')) {
				return false;
			}
			int x2 = x + k;
			int y2 = y - k;
			if (inRange(x2, y2) && (grid[x2][y2] == '+' || grid[x2][y2] == 'o')) {
				return false;
			}
		}
		return true;
		
		
	} else {
		assert(c == 'o');
		return canPlace('x', x, y) && canPlace('+', x, y);
	}
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		//cout << "Case #";
		int M;
		cin >> N >> M;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				grid[i][j] = origGrid[i][j] = '.';
			}
		}
		for (int i = 0; i < M; i++) {
			char ch;
			int r, c;
			cin >> ch >> r >> c;
			grid[r][c] = origGrid[r][c] = ch;
		}
		
		//dispGrid();
		
		// (1) for each position, try to place x (or o)
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (grid[i][j] == '.' && canPlace('x', i, j)) {
					grid[i][j] = 'x';
				}
				if (grid[i][j] == '+' && canPlace('x', i, j)) {
					grid[i][j] = 'o';
				}
			}
		}
		
		// expect total number of x's and o's to equal N
		int cnt = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (grid[i][j] == 'x' || grid[i][j] == 'o') {
					cnt++;
				}
			}
		}
		//assert(cnt == N);
		
		// (2) spiral around the edges, try to place +
		for (int k = 0; k <= (N+1)/2; k++) {
			for (int i = k+1; i <= N-k; i++) {
				int j = k+1;
				if (grid[i][j] == '.' && canPlace('+', i, j)) {
					grid[i][j] = '+';
				}
				if (grid[i][j] == 'x' && canPlace('+', i, j)) {
					grid[i][j] = 'o';
				}
				j = N-k;
				if (grid[i][j] == '.' && canPlace('+', i, j)) {
					grid[i][j] = '+';
				}
				if (grid[i][j] == 'x' && canPlace('+', i, j)) {
					grid[i][j] = 'o';
				}
			}
			for (int j = k+1; j <= N-k; j++) {
				int i = k+1;
				if (grid[i][j] == '.' && canPlace('+', i, j)) {
					grid[i][j] = '+';
				}
				if (grid[i][j] == 'x' && canPlace('+', i, j)) {
					grid[i][j] = 'o';
				}
				i = N-k;
				if (grid[i][j] == '.' && canPlace('+', i, j)) {
					grid[i][j] = '+';
				}
				if (grid[i][j] == 'x' && canPlace('+', i, j)) {
					grid[i][j] = 'o';
				}
			}
		}
		
		
		
		// (2) for each position, try to place +
		// order matters go down left, then up right
		//for (int k = 1; k <= N; k++) {
			//for (int i = 1; i <= k; i++) {
				//int j = k-i+1;
				//if (grid[i][j] == '.' && canPlace('+', i, j)) {
					//grid[i][j] = '+';
				//}
			//}
		//}
		//for (int k = 1; k <= N; k++) {
			//for (int i = N; i >= k; i--) {
				//int j = k+N-i;
				//if (grid[i][j] == '.' && canPlace('+', i, j)) {
					//grid[i][j] = '+';
				//}
			//}
		//}
		
		
		//for (int i = 1; i <= N; i++) {
			//for (int j = 1; j <= N; j++) {
				//if (grid[i][j] == '.' && canPlace('+', i, j)) {
					//grid[i][j] = '+';
				//}
			//}
		//}
		
		// (3) for each x/+, try to upgrade to o
		//for (int i = 1; i <= N; i++) {
			//for (int j = 1; j <= N; j++) {
				//if (canPlace('o', i, j)) {
					//grid[i][j] = 'o';
				//}
			//}
		//}
		
		//dispGrid();
		
		// compute result (score should be 3N-1 for N > 1)
		int score = 0;
		int diff = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (grid[i][j] == 'o') score += 2;
				if (grid[i][j] == 'x' || grid[i][j] == '+') score++;
				if (grid[i][j] != origGrid[i][j]){
					diff++;
				}
			}
		}
		cout << "Case #" << icase << ": " << score << " " << diff << endl;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (grid[i][j] != origGrid[i][j]){
					cout << grid[i][j] << " " << i << " " << j << endl;
				}
			}
		}
	}
	return 0;
}
