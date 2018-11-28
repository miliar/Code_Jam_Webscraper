#include <iostream>
#include <string>

using namespace std;

char cake[25][25];
int row[27];
int col[27];

int main() {
	int T;
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		int R, C;
		cin >> R >> C;
		int nLetters = 0;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++) {
				cin >> cake[i][j];
				if (cake[i][j] != '?') {
					row[nLetters] = i;
					col[nLetters] = j;
					nLetters++;
				}
			}
		
		int rowStart, rowEnd;
		int colStart, colEnd;
		for (int iLetter = 0; iLetter < nLetters; iLetter++) {
			rowStart = row[iLetter];
			rowEnd = row[iLetter];
			colStart = col[iLetter];
			colEnd = col[iLetter];
			while (colStart >= 1 && cake[rowStart][colStart-1] == '?')
				colStart--;
			while (colEnd < C-1 && cake[rowStart][colEnd+1] == '?')
				colEnd++;
			bool freeCell = true;
			while (freeCell && (rowStart >= 1)) {
				for (int iCol = colStart; iCol <= colEnd; iCol++) {
					if (cake[rowStart-1][iCol] != '?') {
						freeCell = false;
						break;
					}
				}
				if (freeCell)
					rowStart--;
			}
			freeCell = true;
			while (freeCell && (rowEnd < R-1)) {
				for (int iCol = colStart; iCol <= colEnd; iCol++) {
					if (cake[rowEnd+1][iCol] != '?') {
						freeCell = false;
						break;
					}
				}
				if (freeCell)
					rowEnd++;
			}
			for (int iCol = colStart; iCol <= colEnd; iCol++)
				for (int iRow = rowStart; iRow <= rowEnd; iRow++)
					cake[iRow][iCol] = cake[row[iLetter]][col[iLetter]];
		}
		
		cout << "Case #" << iCase << ": " << endl;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++)
				cout << cake[i][j];
			cout << endl;
		}
	}
}
