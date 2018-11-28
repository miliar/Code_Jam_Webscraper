#include <iostream>

using namespace std;

int main(){
	int numOfCases;
	cin >> numOfCases;
	for (int cases = 1; cases <= numOfCases; cases++){
		int row, col;
		cin >> row;
		cin >> col;

		char cake [row][col];
		for (int i = 0; i < row; i++) {
			cin >> cake[i];
		}
		for (int i = 0; i < row; i++){
			bool blank = true;
			int j = 0;
			for (; j < col; j++){
				if (cake[i][j] != '?'){
					blank = false;
					break;
				}
			}
			if (blank)
				continue;
			for (int k = 0; k < j; k++){
				cake[i][k] = cake[i][j];
			}
			char initial = cake[i][j];
			for (int k = j + 1; k < col; k++){
				if (cake[i][k] == '?'){
					cake[i][k] = initial;
				} else {
					initial = cake[i][k];
				}
			}
			
			
		}
		for (int i = 0; i < row; i++) {
			if (cake[i][0] == '?' && i - 1 >= 0){
				for (int j = 0; j < col; j++) {
					cake[i][j] = cake[i-1][j];
				}
			} 
		}
		for (int i = row - 1; i >= 0; i--) {
			if (cake[i][0] == '?' && i + 1 < row){
				for (int j = 0; j < col; j++) {
					cake[i][j] = cake[i+1][j];
				}
			} 
		}
		cout << "Case #" << cases << ":" << endl;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}