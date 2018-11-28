// ConsoleApplication3.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define COMPETITION

int main() {

#ifdef COMPETITION
	ifstream infile;
	ofstream outfile;
	infile.open("input.in");
	outfile.open("output.out");
#else
#define infile cin
#define outfile cout
#endif

	int t;
	infile >> t;

	string nStr;
	int r, c;
	char **cake;
	for (int i = 0; i < t; i++) {
		infile >> r >> c;

		cake = new char*[r];
		char found = '?';
		for (int x = 0; x < r; x++) {
			cake[x] = new char[c];
			int findex = -1;
			found = '?';
			for (int y = 0; y < c; y++) {
				if (y > findex) {
					infile >> cake[x][y];
				} 
				if (cake[x][y] != '?') {
					found = cake[x][y];
					if (y > findex) {
						findex = y;
						if (y > 0 && cake[x][y-1]=='?') {
							y -= 2;
						}
					}
				}
				else if (found != '?') {
					cake[x][y] = found;
					if (y > 0 && cake[x][y - 1] == '?') {
						y -= 2;
					}
				}
			}
		}
		for (int y = 0; y < c; y++) {
			int findex = -1;
			found = '?';
			for (int x = 0; x < r; x++) {
				if (cake[x][y] != '?') {
					found = cake[x][y];
					if (x > findex) {
						findex = x;
						if (x > 0 && cake[x-1][y] == '?') {
							x -= 2;
						}
					}
				}
				else if (found != '?') {
					cake[x][y] = found;
					if (x > 0 && cake[x-1][y] == '?') {
						x -= 2;
					}
				}
			}
		}

		outfile << "Case #" << i + 1 << ":" << endl;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				outfile << cake[i][j];
			}
			outfile << "\n";
		}

		for (int x = 0; x < r; x++) delete cake[x];
		delete[] cake;
	}

#ifdef COMPETITION
	outfile.close();
	infile.close();
#else
	cin >> t;
#endif
	return 0;
}
