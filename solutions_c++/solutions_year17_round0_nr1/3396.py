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
		
		string p;
		int k, n;
		input >> p >> k;
		n = 0;
		cout << p << endl;
		for(int i = 0; i < p.length() - k + 1; i++)
		{
			if(p[i] == '-')
			{
				n++;
				for(int j = i; j < i + k; j++)
				{
					if(p[j] == '-')
					{
						p[j] = '+';
					}
					else
					{
						p[j] = '-';
					}
				}
			}
			cout << p << endl;
		}
		if(p.find('-') == -1)
		{
			output << n;
		}
		else
		{
			output << "IMPOSSIBLE";
		}
		
		output << endl;
	}
	output.close();
	input.close();
	return 0;
}