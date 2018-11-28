#include <bits/stdc++.h>
using namespace std;
int testCount;
int R, C;
string board[30];

int main() {
	
	cin >> testCount;
	for (int test = 1; test <= testCount; ++test) {
		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			cin >> board[i];
			
		for (int i = 1; i < R; ++i)
		for (int j = 0; j < C; ++j)
			if (board[i][j] == '?')
				board[i][j] = board[i - 1][j];
				
		for (int i = R - 2; i >= 0; --i)
		for (int j = 0; j < C; ++j)
			if (board[i][j] == '?')
				board[i][j] = board[i + 1][j];				
		
		for (int j = 1; j < C; ++j)
		for (int i = 0; i < R; ++i)
			if (board[i][j] == '?')
				board[i][j] = board[i][j - 1];
				
		for (int j = C - 2; j >= 0; --j)
		for (int i = 0; i < R; ++i)
			if (board[i][j] == '?')
				board[i][j] = board[i][j + 1];
		
		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < R; ++i)		
			cout << board[i] << endl;
	}
	
	return 0;
}
