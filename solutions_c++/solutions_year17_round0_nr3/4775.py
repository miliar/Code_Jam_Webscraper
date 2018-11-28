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
	bool changed;
	int n, k, y, z, pos;
	for (int i = 0; i < t; i++) {
		infile >> n >> k;
		pos = 0;
		for (int j = 0; pow(2, j) <= k; j++) {
			y = ceil((n - 1) / 2.0);
			z = floor((n - 1) / 2.0);

			int tmp = floor(1.0*k / pow(2, j));
			n = tmp % 2 == 0 ? y : z;
		}

		outfile << "Case #" << i + 1 << ": " << y << " " << z << endl;
	}

#ifdef COMPETITION
	outfile.close();
	infile.close();
#else
	cin >> t;
#endif
	return 0;
}
