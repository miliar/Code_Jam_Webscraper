// ConsoleApplication3.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define COMPETITION

int main(){

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

	char s;
	int moves, change, K;
	string Str;
	bool negate, happy;
	int uses[1000] = {0};
	for (int i = 0; i < t; i++) {
		infile >> Str >> K;
		moves = 0;
		negate = false;
		for (int i = 0; i < Str.length(); i++) {
			s = Str[i];
			if (negate) happy = s == '-';
			else happy = s == '+';
			if (moves > 0) {
				for (int k = moves - 1; k >= 0 && uses[k] > 0; k--) {
					uses[k]--;
					if (uses[k] == 0)
						negate = !negate;
				}
			}

			if (!happy) {
				uses[moves] = K-1;
				negate = !negate;
				moves++;
				//cout << "unhappy " << i << endl;	
			}
			//cout << " " << uses[moves - 1] << endl;
		}
		bool possible = moves==0 || uses[moves - 1] == 0;
		if(possible)
			outfile << "Case #" << i + 1 << ": " << moves << endl;
		else
			outfile << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}

#ifdef COMPETITION
	outfile.close();
	infile.close();
#else
	cin >> t;
#endif
    return 0;
}
