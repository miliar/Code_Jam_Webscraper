// tidy.cpp : Defines the entry point for the console application.
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

using namespace std;

int _DBG_LOG_ = 0;

string find_tidy(string);

int main(int argc, char* argv[])
{
	// inputs
	int T;
	vector<string> N;

	int from_file = 1;

	string inFileName = "D:\\DEV\\VS2012\\GoogleCodeJam\\201704\\02\\tidy\\input.txt";

	ifstream inFile(inFileName);

	if(!from_file)
	{
		cin >> T;
	}
	else 
	{
		inFile >> T;
	}

	for(int i = 0; i < T; i++)
	{
		string n;

		if(!from_file)
		{
			cin >> n;
		}
		else
		{
			inFile >> n;
		}

		N.push_back(n);
	}

	for(int i = 0; i < T; i++)
	{
		string cnt = find_tidy(N[i]);
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
}

string find_tidy(string N)
{
	string maxN = N;

	int min_digit = N[N.length() - 1] - '0';

	for(int i = N.length() - 2; i >= 0; i--)
	{
		if(N[i] - '0' > min_digit)
		{
			maxN[i] = N[i] - 1;

			// all others 9
			for(unsigned j = i + 1; j < N.length(); j++)
			{
				maxN[j] = '9';
			}
		}

		min_digit = maxN[i] - '0';
	}

	if(maxN[0] == '0')
	{
		return maxN.substr(1, maxN.length() - 1);
	}

	return maxN;
}
