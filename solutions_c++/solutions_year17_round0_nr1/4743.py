// google_code_jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int _tmain(int argc, _TCHAR* argv[])
{
	int t, k;
	string row;
	cin >> t;  
	for (int i = 1; i <= t; ++i) {
		cin >> row >> k;  
		int rowLength = row.length();
		int numFlips = 0;

		int firstBlankPos = 0;
		while (1) {
			while (firstBlankPos < rowLength && row[firstBlankPos] != '-') {
				firstBlankPos++;
			}
			
			if (firstBlankPos == rowLength) {
				cout << "Case #" << i << ": " << numFlips << endl;
				break;
			}
			else if (firstBlankPos + k > rowLength) {
				cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
				break;
			}
			else {
				for (int m = firstBlankPos; m < firstBlankPos + k; m++) {
					row[m] = row[m] == '+' ? '-' : '+';
				}
				numFlips++;
			}
		}
	}

	return 0;
}

