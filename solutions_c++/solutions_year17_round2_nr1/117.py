// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string> 
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;


int main(int argc, char* argv[])
{
	
	fstream In("a-large.in", ios::in);
	fstream Out("a-large.out", ios::out);

	int cases;
	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		double D;
		int N;
		In >> D >> N;
		double ret = 1e-16;

		for (int i = 0; i < N; i++)
		{
			int Ki, Si;
			In >> Ki >> Si;
			double arrivalTime = (D - Ki) / Si;
			ret = max(ret, arrivalTime);
		}


		Out << "Case #" << (h + 1) << ": " <<setprecision(8) <<  D/ret << endl;
	}

	return 0;
}

