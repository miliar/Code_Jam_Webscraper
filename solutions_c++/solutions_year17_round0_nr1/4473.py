// OversizedPancakeFlipper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include<string>
#include<fstream>
using namespace std;

bool ifHappy(string s,int len)
{
	for (int i = 0; i < len; i++)
	{
		if (s[i] == '-')
			return false;
	}
	return true;
}

int main() {
	int t;
	string s;
	int k;
	string outputFile = "G:/Code Jam/OversizedPancakeFlipper/output.txt";
	string inputFile = "G:/Code Jam/OversizedPancakeFlipper/A-small-attempt0.in";
	ofstream output;
	ifstream input;

	input.open(inputFile);
	output.open(outputFile);
	input >> t;
	int cas = 1;
	int steps;
	while(t--)
	{
		steps = 0;
		input >> s >> k;
		int len = s.length()-k;
		if (ifHappy(s, len + k))
		{
			output << "Case #" << cas << ": 0\n";			
			cas++;
			continue;
		}
		
		for (int j = 0; j <= len; j++)
		{
			if (s[j] == '-')
			{
				for (int i = 0; i < k; i++)
				{
					if (s[j + i] == '+')
						s[j + i] = '-';
					else
						s[j + i] = '+';
				}
				steps++;
			}
		}
		if (ifHappy(s, len + k))
		{
			output << "Case #" << cas << ": " << steps << "\n";
		}
		else
		{
			output << "Case #" << cas << ": IMPOSSIBLE\n";
		}

		
		cas++;
	}
	input.close();
	output.flush();
	output.close();
	// your code goes here
	return 0;
}

