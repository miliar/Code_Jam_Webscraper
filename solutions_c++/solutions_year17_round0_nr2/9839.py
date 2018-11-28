/** ========================================================================
 * Name        : main.cpp
 * Author      : Iuro Nascimento
 * Version     :
 * Copyright   :
 * Description : 
==========================================================================*/
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <chrono>
#include <thread>


int isTidy(std::string sn); 


int main(int argc, char *argv[])
{
	std::chrono::high_resolution_clock::time_point to = std::chrono::
		high_resolution_clock::now();
	if (argc < 2) {
		printf("usage: %s infile [outfile]\n",argv[0]);
		exit(1);
	}
	char *outfname;
	if (argc > 2)
		outfname = argv[2];
	else
		outfname = (char*)"test.out";

	// unsigned int nthreads = std::thread::hardware_concurrency();
	std::string infilename(argv[1]);
	std::string line;
	std::ifstream infile (infilename);
	std::ofstream outfile (outfname);

	if (!infile.is_open()) {
		printf("Unable to open file");
		exit(1);
	}

	unsigned int T, i;
	unsigned long n;
	infile >> T;
	std::string sn;
	int d;
	// int digits[10] = {0};#<{(| compiled with gcc 5.3 |)}>#
	for (i = 0; i < T; i++) {
		infile >> sn;
		n = std::stol(sn);
		while((d = isTidy(sn))>=0) {
			// std::cout << sn << std::endl;
			sn[d-1]-=1;
			for(int j=d;j<sn.length();j++)
				sn[j] = '9';
		}
		// std::cout << "Case #" << i+1 << ": " << std::stol(sn) << std::endl;
		outfile << "Case #" << i+1 << ": " << std::stol(sn) << std::endl;
		// outfile < seq << "\n";
	}
	infile.close();
	outfile.close();

	std::chrono::high_resolution_clock::time_point tf = std::chrono::
		high_resolution_clock::now();
	std::chrono::duration<double,std::ratio<1l,1000000l>> delta_t = 
		std::chrono::duration_cast<std::chrono::duration<double,std::ratio<1l,1000000l>>>(tf - to);

	// std::cout << "Elapsed: " << delta_t.count() << " us.\n";

	return 0;
}

int isTidy(std::string sn)
{
	char old;
	old = sn[0];
	int i = 0;
	for(char &c : sn) {
		// std::cout << c << std::endl;
		if (c < old) {
			// std::cout << "tidy = " << i << std::endl;
			return i;
		}
		old = c;
		i++;
	}

	return -1;
}
