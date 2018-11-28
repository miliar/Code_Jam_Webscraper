// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int func(string s, int kk)
{
	size_t pos = s.find("-");
	if (pos == string::npos)
	{
		return 0;
	}
	else if (s.size() - pos < kk)
	{
		return -1;
	}

	for (int i = 0; i < kk; i++)
	{
		if (s[pos+i] == '-')
			s[pos+i] = '+';
		else
			s[pos+i] = '-';
	}

	int new_pos = s.find("-");
	if (new_pos == string::npos)
		return 1;

	int new_res = func(s.substr(new_pos, s.size() - new_pos), kk);
	if (new_res < 0)
		return -1;

	return new_res + 1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("a.in");
	ofstream fo("a.out");

	int t;
	fi >> t;

	for (int i = 0; i < t; i++)
	{
		int k = 0;
		string str;
		fi >> str >> k;

		int res = func(str, k);
		fo << "Case #" << i+1 << ": ";
		if (res < 0)
			fo << "IMPOSSIBLE" << endl;
		else
			fo << res << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

