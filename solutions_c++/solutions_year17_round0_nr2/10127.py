// B.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>


bool isTidy(std::string S) {
	bool _isTidy = true;
	for (double idx = 0; idx < S.size() - 1; idx++) {
		if (S[idx] > S[idx + 1]) {
			_isTidy = false;
			break;
		}
	}
	return _isTidy;
}


int main() {
	//Open the file
	std::ifstream infile;
	infile.open("B-small-attempt0.in");
	std::ofstream  outfile;
	outfile.open("B-small-attempt0.out");

	//Read the number of cases
	int T, count = 1;
	infile >> T;

	while (T-- > 0) {
		std::string N;
		infile >> N;

		//Find next tidy element
		std::string nearTidy = N;
		while (!isTidy(nearTidy)) {
			//Reduce 1 to tidy
			for (int i = nearTidy.size() - 1; i >= 0; i--) {
				if (nearTidy[i] != '0') {
					nearTidy[i] = nearTidy[i] - 1;
					break;
				}
				else {
					nearTidy[i] = '9';
				}
			}
		}
		
		outfile << "Case #" << count++ << ": " << std::stoi(nearTidy) << (T>0 ? "\n" : "");

	}

	return 0;
}

