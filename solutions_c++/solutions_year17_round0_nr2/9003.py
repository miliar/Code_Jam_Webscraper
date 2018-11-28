// TidyNumber.cpp : Defines the entry point for the console application.
//

// TidyNumber.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");

bool checkNumber(string number)
{
	int n = number.size();
	int i;
	for (int j = 0; j < n-1; j++)
	{
		i = j + 1;
		if (number[i] >= number[j])
			continue;
		else
			return false;
	}
	return true;
}
int main()
{
	int T;
	fin >> T;
	int ct = 1;
	string number;
	while (T--)
	{
		
		fin >> number;
		int n = number.size();
		int j = 0;

		while (!checkNumber(number))
		{
			for (int j = 0; j < n; j++)
			{
				if (number[j] > number[j + 1])
				{
					number[j]--;

					for (int k = j + 1; k < n; k++)
					{
						if (number[k] == '9')continue;
						else
							number[k] = '9';
					}
					break;
				}
			}
		}
		int start;
		if (number[0] == '0')
			start = 1;
		else
			start = 0;
		

		string out = "";
		for (int i = start; i < n; i++)
			out += number[i];
		fout << "Case #" << ct << ": "<<out<<endl;
		//cout << endl;
		ct++;
	}
return 0;
}

