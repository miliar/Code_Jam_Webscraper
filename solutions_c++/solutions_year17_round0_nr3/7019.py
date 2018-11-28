// C.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>

//Iterate all Stall's and find the one with max Ls and Rs
std::vector<std::string> findFreeStall(std::vector<std::string> Stall, double &Ls, double &Rs) {
	//Create variables
	std::vector<std::string> newStall = Stall;
	int idx_max_size = -1, max_size = -1;

	//Find the longest string
	for (int index = 0; index < Stall.size(); ++index) {
		int stallSize = Stall[index].size();
		if (stallSize > max_size) {
			max_size = stallSize;
			idx_max_size = index;
		}
	}

	//Split the string into 2 strings	
	int idx_client = floor((Stall[idx_max_size].size() - 1) / 2.0);
	Stall[idx_max_size][idx_client] = '1';
	std::string left = Stall[idx_max_size].substr(0, idx_client+1);
	std::string right = Stall[idx_max_size].substr(idx_client, Stall[idx_max_size].size()-1);

	//Calculate Ls and Rs
	Ls = left.size() - 2;
	Rs = right.size() - 2;

	//Insert the new 2 strings and delete the old
	newStall.insert(newStall.begin() + idx_max_size + 1, left);
	newStall.insert(newStall.begin() + idx_max_size + 2, right);
	newStall.erase(newStall.begin() + idx_max_size);

	return newStall;
}

int main() {

	//Open the file
	std::ifstream infile;
	infile.open("C-small-1-attempt1.in");
	std::ofstream  outfile;
	outfile.open("C-small-1-attempt1.out");

	//Read the number of cases
	int T, count = 1;
	infile >> T;

	while (T-- > 0) {
		double K, N;
		infile >> N;
		infile >> K;

		//Insert the Stalls into the vector
		std::vector<std::string> Stalls;

		//Create the stalls and fill with guards
		std::string init_Stalls(N+2, '0');
		init_Stalls[0] = '1';
		init_Stalls[N + 1] = '1';
		//Push into the Stalls
		Stalls.push_back(init_Stalls);

		//Init Ls, Rs and their max/min
		double Ls = 0, Rs = 0;

		//Clients input
		while (K-- > 0) {
			Stalls = findFreeStall(Stalls, Ls, Rs);
		}

		//Output
		outfile << "Case #" << count++ << ": " << std::max(Ls, Rs) << " " << std::min(Ls, Rs) << (T>0 ? "\n" : "");


	}
    return 0;
}

