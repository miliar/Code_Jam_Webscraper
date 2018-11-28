#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;


int main()
{
	ifstream inputFile("A-large.in");
	ofstream outputFile("output_2017.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{ 
		outputFile << "Case #" << i << ": ";
		unsigned long long d;
		unsigned long long n;

		std::vector<double> arrival;

		inputFile >> d;
		inputFile >> n;

		for (int j = 0; j < n; ++j)
		{
			int k, s;

			inputFile >> k;
			inputFile >> s;

			unsigned long long distanceLeft = d - k;
			arrival.push_back((double)distanceLeft / (double)s);
		}

		double res = *std::max_element(arrival.begin(), arrival.end());

		
		outputFile << setprecision(6) << fixed << (double)d / res << endl;
	}

	return 0;
}
