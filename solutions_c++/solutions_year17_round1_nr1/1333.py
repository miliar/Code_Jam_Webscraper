#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,rows,columns;
	char grid [30][30];
	char let;
	bool seen;
	
	cin >> T;
	for (int testCase = 1 ; testCase <= T; ++testCase){
		cin >> rows >> columns;
		for (int i = 0 ; i < rows;++i){
			for (int j = 0; j < columns;++j){
				cin >> let;
				grid[i][j] = let;
			}
		}
		
		
		for (int j = 0 ; j < columns;++j){
			seen = false;
			for (int i = 0; i < rows;++i){
				if (grid[i][j] != '?'){
					seen = true;
					let = grid[i][j];
				}
				else if (seen){
					grid[i][j] = let;
				}
			}
			seen = false;
			for (int i = rows-1; i >=0;--i){
				if (grid[i][j] != '?'){
					seen = true;
					let = grid[i][j];
				}
				else if (seen){
					grid[i][j] = let;
				}
			}
		}
		
		for (int j = 0 ; j < rows;++j){
			seen = false;
			for (int i = 0; i < columns;++i){
				if (grid[j][i] != '?'){
					seen = true;
					let = grid[j][i];
				}
				else if (seen){
					grid[j][i] = let;
				}
			}
			seen = false;
			for (int i = columns-1; i >=0;--i){
				if (grid[j][i] != '?'){
					seen = true;
					let = grid[j][i];
				}
				else if (seen){
					grid[j][i] = let;
				}
			}
		}
		
		printf("Case #%d:\n",testCase);	
		for (int i = 0 ; i < rows;++i){
			for (int j = 0; j < columns;++j){
				cout << grid[i][j];
			}
			cout <<endl;
		}
		
	}
	return 0;
}
