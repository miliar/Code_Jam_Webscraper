#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main() {
	int T,R,C;
	char initial;
	vector<vector<char>> cake;
	string S;
	ifstream infile("A-large.in");
	ofstream outfile("outputlargeA.txt");

	infile >> T;

	for (int t = 0; t < T; t++) { //for every test case
		outfile << "Case #" << t + 1 << ":\n";

		infile >> R >> C;
		cake.clear();

		for (int i = 0; i < R; i++) {
			vector<char> temp;
			for (int j = 0; j < C; j++) {
				infile >> initial;
				temp.push_back(initial);
				
			}
			cake.push_back(temp);
		}

			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					char cc = cake[i][j];
					if (cc != '?') {
						for (int k = 1; k < C - j;k++) {
							if (cake[i][j + k] != '?') break;
							cake[i][j + k] = cc;
						}
						for (int k = 1; k - j <= 0; k++) {
							if (cake[i][j-k] != '?') break;
							cake[i][j - k] = cc;
						}
					}
				}
			}
	
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					char cc = cake[i][j];
					if (cc != '?') {
						for (int k = 1; k < R - i; k++) {
						if (cake[i+k][j] != '?') break;
						cake[i+ k][j] = cc;
						}

						for (int k = 1; k - i <= 0; k++) {
							if (cake[i - k][j] != '?') break;
							cake[i - k][j] = cc;
						}
					}
				}
			}


		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				outfile << cake[i][j];
			}
			outfile << endl;
		}

//		outfile << S << "\n";
	}
	return 0;
}