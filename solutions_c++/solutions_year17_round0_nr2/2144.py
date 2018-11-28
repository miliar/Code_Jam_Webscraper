// Google2017Q-B.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	input.open("B-large.in", std::ios_base::in);
	output.open("B-large.txt");

	int T;
	input >> T;
	for (int g = 0; g < T; g++)
	{
		string s;
		input >> s;
		int n = s.length();

		output << "Case #" << g + 1 << ": ";

		vector<int> d;
		for (int i = 0; i < n; i++)
			d.push_back(s[i] - '0');

		int j = 0;
		while (j + 1 < n && d[j] <= d[j + 1])
			j++;
		if (j + 1 >= n)
			output << s << "\n";
		else
		{
			// d[j] > d[j+1]
			// ok we must decrease 
			d[j] --;
			while (j > 0 && d[j-1] > d[j])
			{
				j--;
				d[j]--;
			}
			for (int i = j + 1; i < n; i++)
				d[i] = 9;
			j = 0;
			while (d[j] == 0)
				j++;
			for (int i = j; j < n; j++)
				output << d[j];
			output << "\n";
		}
	}
	
	input.close();
	output.close();

	return 0;
}


