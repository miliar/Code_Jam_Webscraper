// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string decrease(string s);

string func(string s)
{
	int pos = -1;
	for (int i = 0; i < s.size() - 1; i++)
	{
		if (s[i] > s[i+1])
		{
			pos = i;
			break;
		}
	}

	if (pos < 0)
	{
		return s;
	}
		
	string str2 = decrease(s.substr(0, pos + 1));
	for (int i = 0; i < s.size() - pos - 1; i++)
		str2 += "9";
	return str2;
}

string decrease(string s)
{
	int size = s.size();
	if (s[size - 1] == '0')
		return decrease(s.substr(0, size - 1)) + "9";

	s[size - 1] = s[size - 1] - 1;
	if ((size == 1) && (s[size - 1] == '0'))
		return "";

	return func(s);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("b.in");
	ofstream fo("b.out");

	int t;
	fi >> t;

	for (int i = 0; i < t; i++)
	{
		string str;
		fi >> str;

		fo << "Case #" << i + 1 << ": " << func(str) << endl;
	}

	fi.close();
	fo.close();

	return 0;
}

