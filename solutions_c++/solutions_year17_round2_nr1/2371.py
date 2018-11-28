// round-1b-1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <iomanip>
using namespace std;

// http://stackoverflow.com/a/236803/3479448
template<typename Out>
void split(const std::string &s, char delim, Out result) {
	std::stringstream ss;
	ss.str(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		*(result++) = item;
	}
}


std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, std::back_inserter(elems));
	return elems;
}

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream inputFile("C:/Users/jnambiar/Documents/main/code-jam/round-1b-1/input.txt");
	ofstream outputFile("C:/Users/jnambiar/Documents/main/code-jam/round-1b-1/output.txt");

	int testCases=0;
	inputFile >> testCases;
	inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i = 0; i < testCases; i++) {
		int D, N;
		inputFile >> D >> N;
		inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		double maxTime = 0;
		for(int j = 0; j < N; j++) {
			int di, si;
			inputFile >> di >> si;
			double time = ((D-di)*1.0)/si;
			if(time > maxTime) {
				maxTime = time;
			}
			inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		}
		double ret = D / maxTime;
		outputFile << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(6) <<ret << endl;
	}
	inputFile.close();
	outputFile.close();

	return 0;
}

