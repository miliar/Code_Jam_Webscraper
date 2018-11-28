#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc != 2)
	{
		cerr << "Error: No file has been specified. Program is terminating." << endl;
		return 0;
	}
	ifstream input(argv[1]);
	if(!input)
	{
		cerr << "Error: No file found at specified location. Program is terminating" << endl;
		return 0;
	}
	int T;
	input >> T;
	ofstream output("out.txt");
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": "; //output test case number
		long double D, N;
		input >> D >> N;
		vector<pair<int, int> > horses;
		for(int i = 0; i < N; i++)
		{
			long double K, S;
			input >> K >> S;
			pair<int, int> horse(K, S);
			horses.push_back(horse);
		}
		long double time = 0.0;
		long double current;
		for(int i = 0; i < N; i++)
		{
			current = ((1.0*(D - horses[i].first))/(1.0*horses[i].second));
			if(current > time)
			{
				time = current;
			}
		}
		time = (D*1.0)/time;
		output << setprecision(16) << time;
		output << endl;
	}
	output.close();
	input.close();
	return 0;
}