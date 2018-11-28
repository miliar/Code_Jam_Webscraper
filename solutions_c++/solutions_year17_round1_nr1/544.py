#include <bits/stdc++.h>
using namespace std;

void test() {
	
	int R, C;
	cin >> R >> C;
	
	vector<string> grid(R);
	for (int i = 0; i < R; ++i) {
		cin >> grid[i];
		
		for (int j = 1; j < C; ++j)
			if (grid[i][j] == '?' && grid[i][j-1] != '?')
				grid[i][j] = grid[i][j-1];
				
		for (int j = C-2; j >= 0; --j)
			if (grid[i][j] == '?' && grid[i][j+1] != '?')
				grid[i][j] = grid[i][j+1];
	}
	
	for (int i = 1; i < R; ++i)
		if (grid[i][0] == '?' && grid[i-1][0] != '?')
			grid[i] = grid[i-1];
			
	for (int i = R-2; i >= 0; --i)
		if (grid[i][0] == '?' && grid[i+1][0] != '?')
			grid[i] = grid[i+1];
	
	
	for (int i = 0; i < R; ++i) {
		cout << endl << grid[i];
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
