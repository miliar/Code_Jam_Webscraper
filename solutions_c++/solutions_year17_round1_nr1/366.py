#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	int R, C;
	cin >> R >> C;
	vector<vector<char>> grid(R,vector<char>(C));
	
	for (int i=0; i<R; i++)
		for (int j=0; j<C; j++)
			cin >> grid[i][j];
	
	// First all rows with something in them
	for (int i=0; i<R; i++) {
		char firstC = '?';
		for (int j=0; j<C; j++) {
			if (grid[i][j] != '?') {
				firstC = grid[i][j];
				break;
			}
		}
		if (firstC == '?') continue;
		for (int j=0; j<C; j++) {
			if (grid[i][j] == '?') {
				grid[i][j] = firstC;
			} else {
				firstC = grid[i][j];
			}
		}
	}
	
	// Then all rows that are empty become copies
	int firstI = 0;
	for (int i=0; i<R; i++) {
		if (grid[i][0] != '?') {
			firstI = i;
			break;
		}
	}
	for (int i=0; i<R; i++) {
		if (grid[i][0] == '?') {
			grid[i] = grid[firstI];
		} else {
			firstI = i;
		}
	}
	
	// Output
	cout << "Case #" << t << ":" << endl;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			cout << grid[i][j];
		}
		cout << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
