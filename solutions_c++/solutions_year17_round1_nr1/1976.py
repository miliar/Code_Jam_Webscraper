#include <iostream>
#include <fstream>
#include <string>
#include <vector>
//#include <algorithm>
//#include <queue>
using namespace std;

void main(){
	int T;
	ifstream infile;
	infile.open("A-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output1A-123444567.txt");
	infile >> T;
	int i = T;
	while (i){
		int R, C;
		infile >> R >> C;
		char c;
		vector<vector<char>> A;
		for (int a = 0; a < R; a++){
			vector <char>B;
			for (int b = 0; b < C; b++){
				infile >> c;
				B.push_back(c);
			}
			A.push_back(B);
		}
		bool empty = false;
		int count = 0;
		do {
			empty = true;
			//count = 0;
			for (int b = 0; b < C && empty; b++){
				empty = (A[count][b] == '?');
			}
			if (empty) count++;
		} while (empty);
		for (int a = count; a < R; a++){
			int c2 = 0;
			while ((c2 < C) ? A[a][c2] == '?' : false) c2++;
			if (c2 == C) A[a] = A[a - 1];
			else{
				for (int b = c2 + 1; b < C; b++){
					if (A[a][b] == '?') A[a][b] = A[a][b - 1];
				}
				for (int b = 0; b < c2; b++){
					A[a][b] = A[a][c2];
				}
			}
		}
		for (int a = 0; a < count; a++){
			A[a] = A[count];
		}
		outfile << "Case #" << T - i + 1 << ":" << endl;
		for (int a = 0; a < R; a++){
			for (int b = 0; b < C; b++){
				outfile << A[a][b];
			}
			outfile << endl;
		}
		i--;
	}
	infile.close();
	outfile.close();
	system("pause");
}