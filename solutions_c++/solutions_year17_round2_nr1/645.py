// q1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;


int main()
{
	ifstream inFile;
	inFile.open("..\\..\\A-large.in");
	//inFile.open("..\\..\\A-large.in");
	ofstream outFile;
	outFile.open("..\\..\\A-large.out");
	//outFile.open("..\\..\\A-large.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		int64_t D;
		size_t N;
		inFile >> D;
		inFile >> N;

		int64_t K;
		int64_t S;
		double max_time = 0;
		for (size_t j = 0; j < N; j++) {
			inFile >> K;
			inFile >> S;
			double t = ((double)D - (double)K) / (double)S;
			if (t > max_time)
				max_time = t;
		}
		double res = (double)D / max_time;

		outFile << std::fixed << std::setprecision(10) << "Case #" << (i + 1) << ": " << res << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}