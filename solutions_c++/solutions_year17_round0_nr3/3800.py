#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>

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
	ofstream output("output.txt");
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": "; //output test case number
		
		unsigned long long int N, K;
		
		input >> N >> K;
		priority_queue<unsigned long long int> space;
		space.push(N);
		unsigned long long int current;
		for(unsigned long long int i = 1; i < K; i++)
		{
			current = space.top();
			space.pop();
			current--;
			space.push(floor(current / 2.0));
			space.push(ceil(current / 2.0));
		}
		current = space.top();
		current--;
		output << ceil(current/2.0) << " " << floor(current/2.0);
		output << endl;
	}
	output.close();
	input.close();
	return 0;
}