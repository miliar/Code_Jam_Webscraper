// Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

string toString(const unsigned long long& n)
{
	stringstream ss;

	ss << n;

	string str;

	ss >> str;

	return str;
}

unsigned long long pow10(unsigned long long base, unsigned long long exponent)
{
	unsigned long long ans = 1;

	for (int i = 0; i < exponent; i++)
		ans *= base;

	return ans;
}

bool isTidy(unsigned long long& n)
{
	string str = toString(n);

	int len = str.size();
	const char* c_str = str.c_str();

	for (int i = 0; i < len - 1; i++)
	{
		if (c_str[i] > c_str[i + 1])
		{
			for (int j = i + 1; j < len; j++)
			{
				n -= (c_str[j] - '0') * pow10(10, len - j - 1);
			}
			return false;
		}
	}

	return true;
}

int main()
{
	ifstream in("B-large.in");
	ofstream out;
	out.open("out.txt");

	int T;

	in >> T;

	for (int i = 1; i <= T; i++)
	{
		out << "Case #" << i << ": ";

		unsigned long long N;

		in >> N;

		for (; N >= 0; N--)
		{
			if (isTidy(N))
			{
				out << N << "\n";
				break;
			}
		}
	}
	in.close();
	out.close();

    return 0;
}

