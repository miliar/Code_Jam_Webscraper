#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define endl '\n'
#define PI acos(-1)
using namespace std;

typedef long long ll;

typedef pair<int, int> coord;
typedef vector<coord> letters;

map<char, letters> cake;
int countBlankCake;
char matrix[30][30];

//0: up, 1: right, 2: down, 3: left
bool move(char c, int direction, int R, int C) {

	char auxMat[30][30];
	letters auxLet = cake[c];

	for(int i = 0; i < 30; i++)
		for(int j = 0; j < 30; j++)
			auxMat[i][j] = matrix[i][j];

	int incRow, incCol;
	switch(direction) {
		case 0: incRow = -1; incCol = 0; break;
		case 1: incRow = 0; incCol = 1; break;
	   	case 2: incRow = 1; incCol = 0; break;
		case 3: incRow = 0; incCol = -1; break;	   
	}
	int s = cake[c].size();
	int count = 0;
	for(int i = 0; i < s; i++) {
		coord curr = cake[c][i];
		curr.fi += incRow;
		curr.se += incCol;
		if(curr.fi < 0 || curr.fi >= R || curr.se < 0 || curr.se >= C)
			return false;
		else if(matrix[curr.fi][curr.se] == matrix[curr.fi - incRow][curr.se - incCol])
			continue;
		else if(matrix[curr.fi][curr.se] != '?')
			return false;
		auxMat[curr.fi][curr.se] = matrix[curr.fi - incRow][curr.se - incCol];
		count++;
		auxLet.pb(curr);
	}

	countBlankCake -= count;
	for(int i = 0; i < 30; i++)
		for(int j = 0; j < 30; j++)
			matrix[i][j] = auxMat[i][j];

	cake[c] = auxLet;

	return true;
}

int main() {

	int T, R, C;
	cin >> T;

	for(int i = 1; i <= T; i++) {

		cin >> R >> C;
		countBlankCake = 0;

		cake.clear();

		for(int j = 0; j < R; j++)
			for(int k = 0; k < C; k++) {
				cin >> matrix[j][k];
				if(matrix[j][k] == '?')
					countBlankCake++;
				else 
					cake[matrix[j][k]].pb(mp(j, k));
			}

		while(countBlankCake > 0) {
//			cout << "count: " << countBlankCake << endl;
			for(map<char, letters>::iterator it = cake.begin(); it != cake.end(); it++) {
				for(int j = 0; j < 4; j++) {
					bool ret = move(it->fi, j, R, C);

/*					if(ret) {
						cout << "-------------" << endl;
						for(int k = 0; k < R; k++) {
							for(int l = 0; l < C; l++)
								cout << matrix[k][l];
							cout << endl;
						}
						cout << "-------------" << endl;
					}*/

				}
			}
//			cin >> aux;
		}

					
		cout << "Case #" << i << ":" << endl;

		for(int j = 0; j < R; j++) {
			for(int k = 0; k < C; k++)
				cout << matrix[j][k];
			cout << endl;
		}

	}
	
	return 0;
}
