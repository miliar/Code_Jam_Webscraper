// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include<string>
#include<fstream>
using namespace std;

bool manString(int start, int end, string& s)
{
	int i = start;
	while (i<end&&s[i] == '1')
		i++;
	if (s[i] == '0')
	{
		for (int j = start; j <= end; j++)
			s[j] = '9';
		return true;
	}
	return false;
}


int main() {
	int t;
	string s;
	string outputFile = "G:/Code Jam/TidyNumbers/output.txt";
	string inputFile = "G:/Code Jam/TidyNumbers/B-small-attempt2.in";
	ofstream output;
	ifstream input;

	input.open(inputFile);
	output.open(outputFile);
	input >> t;
	int k = 1;
	while (t--)
	{
		input >> s;
		string res = "";
		int len = s.length() - 1;
		int i = 0;
		if (s[0] == '1' && manString(0, len, s))
		{
			s[len] = '\n';
			output << "Case #" << k << ": " << s ;
			k++;
			continue;
		}
		bool isDone = false;
		while (i<len)
		{
			if (s[i] > s[i + 1])
			{

				s[i] = s[i] - 1;
				res = res + s[i];
				for (int j = i + 1; j <= len; j++)
				{
					s[j] = '9';
				}
				
				if (i > 0 && s[i - 1] > s[i])
				{
					int j = i;
					while (j > 0 && s[j - 1] > s[j])
					{
						s[j] = '9';
						s[j - 1] = s[j - 1] - 1;
						j--;
					}

				}
				continue;


			}
			else if (s[i] == '1' && manString(i, len, s))
			{
				if (i > 0 && s[i - 1] > s[i])
				{
					int j = i;
					while (j > 0 && s[j - 1] > s[j])
					{
						s[j] = '9';
						s[j - 1] = s[j-1]-1;
						j--;
					}

				}
				continue;
			}
			i++;
		}
		output <<"Case #"<<k<<": "<< s << "\n";
		k++;
	}
	input.close();
	output.flush();
	output.close();
	// your code goes here
	return 0;
}

