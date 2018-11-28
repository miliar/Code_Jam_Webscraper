// cruise.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

int _DBG_LOG_ = 0;

int main(int argc, char* argv[])
{
	// inputs
	int T, D, N, K, S;
	
	string inFileName = "D:\\DEV\\VS2012\\GoogleCodeJam\\20170422\\01\\cruise\\input.txt";

	ifstream inFile(inFileName);
	
	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		inFile >> D >> N;

		double max_t_arr = 0;

		for(int j = 0; j < N; j++)
		{
			inFile >> K >> S;
			double t_arr = (double) (D - K) / S;
			max_t_arr = (t_arr > max_t_arr) ? t_arr : max_t_arr;
		}

		//cout << "Case #" << i + 1 << ": " << setprecision(6) << (double) D / max_t_arr << endl;
		printf("Case #%d: %.6f\n", i+1, (double) D / max_t_arr);
	}


	return 0;
}

