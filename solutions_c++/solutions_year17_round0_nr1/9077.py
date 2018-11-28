// A. Oversized Pancake Flipper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output-large.txt");
	int k, cont = 0, t, f = 0;
	string s;
	fin >> t;
	for (int j = 1; j <= t; j++)
	{
		f = 0, cont=0;

		fin >> s >> k;
		for (int i = 0; i<=s.length() - k; i++)
		{
			if (s[i] == '-')
			{
				cont++;
				for (int m = i; m<k + i; m++)
				{
					if (s[m] == '-')
						s[m] = '+';
					else
						s[m] = '-';
				}
			}
		}
		for (int i = 0; i<s.length(); i++)
		{
			if (s[i] == '-')
			{
				fout << "Case #" << j << ": IMPOSSIBLE" << endl;
				f = 1;
				break;
			}
		}
		if (!f)
			fout << "Case #" << j << ": " << cont << endl;
	}

	return 0;
}
