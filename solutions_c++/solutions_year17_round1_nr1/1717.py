#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int arr[30][30];
long T, col, row;


bool check() {
	for(int i = 0 ; i < row; i++) {
		for(int j = 0 ; j < col; j++) {
			if( arr[i][j] == -1) return false;
		}
	}

	return true;
}

void solve() {


	for(int i = 0 ; i < row*col; i++) {
		for(int j = 0 ; j < row; j++) {
			for(int k = 0 ; k < col; k++) {
				if( j + 1 < row && arr[j][k] == -1 && arr[j+1][k] != -1)
					arr[j][k] = arr[j+1][k];

				if( j - 1 >= 0 && arr[j][k] == -1 && arr[j-1][k] != -1)
					arr[j][k] = arr[j-1][k];
			}
		}
	}


	for(int i = 0 ; i < row*col; i++) {
		for(int j = 0 ; j < row; j++) {
			for(int k = 0 ; k < col; k++) {
				if( k + 1 < col && arr[j][k] == -1 && arr[j][k+1] != -1)
					arr[j][k] = arr[j][k+1];

				if( k - 1 >= 0 && arr[j][k] == -1 && arr[j][k-1] != -1)
					arr[j][k] = arr[j][k-1];
			}
		}
	}

}

int main() {

	string sLine;

	cin >> T;

	ofstream outfile;
   	outfile.open("ans.txt");


	for (int currentTest = 0; currentTest < T; ++currentTest)
	{


		outfile << "Case #" << (currentTest+1) << ": ";

		cin >> row >> col;

		for(int i = 0 ; i < row; i++) {

			cin >> sLine;

			for(int j = 0 ; j < col; j++)
				arr[i][j] = ( ( sLine[j] == '?' ) ? -1 : sLine[j] - 'A');
		
		}

		solve();

		outfile << endl;

		for(int i = 0 ; i < row; i++) {
				for(int j = 0 ; j < col; j++) {
					outfile << (char) (arr[i][j] + 'A');
				}
				outfile << endl;
			}		
	}

	outfile.close();

	return 0;
}