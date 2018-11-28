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

	string nStr;
	bool changed;
	for (int i = 0; i < t; i++) {
		infile >> nStr;
		changed = false;
		for (int i = 0; i < nStr.length(); i++) {
			if (changed)
				nStr[i]='9';
			else if ( i + 1 < nStr.length() && nStr[i] > nStr[i+1]) {
				nStr[i] = nStr[i]-1;
				if (i - 1 >= 0 && nStr[i - 1] > nStr[i])
					i -= 2;
				else
					changed = true;
			}
		}
		if (nStr[0] == '0') nStr = nStr.substr(1);
		outfile << "Case #" << i + 1 << ": " << nStr << endl;
	}

#ifdef COMPETITION
	outfile.close();
	infile.close();
#else
	cin >> t;
#endif
    return 0;
}
