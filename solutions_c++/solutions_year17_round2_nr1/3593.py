

#include "stdafx.h"
#include <iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
#include <iomanip>
using namespace std;

bool comp(pair<long int, double> p1, pair<long int, double> p2)
{
	if (p1.first > p2.first ||(p1.first == p2.first && p1.second>p2.second))
		return 1;
	return 0;
}

int main() {
	int t;
	long int d;
	int n;
	string outputFile = "G:/Code Jam/round1B/CruiseControl/output.txt";
	string inputFile = "G:/Code Jam/round1B/CruiseControl/A-small-attempt1.in";
	ofstream output;
	ifstream input;

	input.open(inputFile);
	output.open(outputFile);
	input >> t;
	int cas = 1;
	long int k;
	long int s;
	double hours;
	int r, c;
	while (t--)
	{
		input >> d >> n;
		double maxHours = 0.000000000001;
		for (int i = 0; i < n; i++)
		{
			input >> k >> s;
			hours = (double)(d - k) / (double)s;
			if (hours > maxHours)
			{
				maxHours = hours;
			}

		}
		output << "Case #" << cas << ": " <<fixed<< setprecision(6) << (double)d / maxHours<<"\n" ;
		cas++;

	}
	input.close();
	output.flush();
	output.close();
	
	// your code goes here
	return 0;
}

