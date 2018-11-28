


#include "stdafx.h"

#include <iostream>


#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#define ffor(a,b,c) for(int (a)=(b);(a)<(c);(a)++)


int main()
{

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	int NN; infile >> NN;

	ffor(iy, 1, NN + 1) {

		int R, C;
		infile >> R >> C;
		std::string in[35];
		ffor(i, 0, R)infile >> in[i];
		//R = 5; C = 10;
		//in[0] = "??????????";
		//in[1] = "??C???D???";
		//in[2] = "????G?????";
		//in[3] = "?E???F????";
		//in[4] = "??????????";

		int nonR, nonC;

		bool found = false;
		ffor(i, 0, R) {
			ffor(j, 0, C) {
				if (in[i][j] != '?') { 
					nonR = i; nonC = j;
					found = true;
					break;
				}
			}
			if (found)break;
		}
		for (int j = nonC - 1; j >= 0; j--) {
			if (in[nonR][j] == '?')in[nonR][j] = in[nonR][j + 1];
		}
		for (int j = nonC + 1; j <C; j++) {
			if (in[nonR][j] == '?')in[nonR][j] = in[nonR][j - 1];
		}


		for (int i = nonR - 1; i >= 0; i--) {
			in[i] = in[i + 1];

		}
		for (int i = nonR + 1; i <R ; i++) {
			bool empty = true;
			ffor(j, 0, C) {
				if (in[i][j] != '?') { nonC = j; empty = false; }
			}
			if (empty)in[i] = in[i - 1];
			else {
				for (int j = nonC - 1; j >= 0; j--) {
					if (in[i][j] == '?')in[i][j] = in[i][j + 1];
				}
				for (int j = nonC + 1; j <C; j++) {
					if (in[i][j] == '?')in[i][j] = in[i][j - 1];
				}
			}
		}


		outfile << "Case #" << iy << ": " << " " << std::endl;
		ffor(i, 0, R) outfile << in[i] << std::endl;


	}

	return 0;
}

