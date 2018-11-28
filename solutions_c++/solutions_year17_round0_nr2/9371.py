// ConsoleApplication2.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include<stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int intocha(char f)
{
	int result;
	f -= '0';
	result = f;
	return result;
}

bool isTidy(long long num, long long *j)
{
	bool tidy = true;
	string str;
	string extra;
	long long extrabit;
	char c;
	short cur, last = 0;

	str = to_string(num);

	for (int i = 0; i < str.length(); i++)
	{
		c = str[i];
		cur = intocha(c);

		if (cur > last) last = cur;

		if (cur < last)
		{
			tidy = false;
			extra = str.substr(i, str.length() - i);
			extrabit = stoll(extra);
			*j += extrabit;
			break;
		}
	}
	return tidy;
}

int main()
{
	int i, T;
	long long N;

	cin >> T;

	for (i = 0; i < T; i++)
	{
		cin >> N;

		for (long long j = 0; j < N; j++)
		{
			if (isTidy(N - j, &j))
			{
				cout << "Case #" << i+1 << ": " << N - j << endl;
				break;
			}
		}
	}
	return 0;
}
