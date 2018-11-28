#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>

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
		
		string S;
		input >> S;
		
		int last = 0;
		for(int i = 1; i < S.length(); i++)
		{
			if(S[i] < S[last])
			{
				S[last]--;
				for(int j = last + 1; j < S.length(); j++)
				{
					S[j] = '9';
				}
				break;
			}
			else if(S[i] > S[last])
			{
				last = i;
			}
		}
		if(S[0] == '0' && S.length() != 1)
		{
			S = S.substr(1);
		}
		output << S;
		
		
		output << endl;
	}
	output.close();
	input.close();
	return 0;
}