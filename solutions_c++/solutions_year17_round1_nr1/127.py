#include<iostream>

using namespace std;

int R,C;
char grid[25][25];

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		cin >> R >> C;
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++)
				cin >> grid[i][j];
		
		//Fill started rows
		for (int i=0; i<R; i++) {
			char cur='?';
			for (int j=0; j<C; j++) {
				if (grid[i][j] != '?') {
					cur = grid[i][j];
					break;
				}
			}


			for (int j=0; j<C; j++) {
				if (grid[i][j] != '?')
					cur = grid[i][j];
				grid[i][j] = cur;
			}
		}

		//Fill empty rows
		int copy=0;
		for (int i=0; i<R; i++) { 
			if (grid[i][0] != '?') {
				copy = i;
				break;
			}
		}

		for (int i=0; i<R; i++) {
			if (grid[i][0] != '?')
				copy = i;

			for (int j=0; j<C; j++)
				grid[i][j] = grid[copy][j];
		}

		cout << "Case #" << T << ":\n";
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) 
				cout << grid[i][j];
			cout << "\n";
		}
	}
}
