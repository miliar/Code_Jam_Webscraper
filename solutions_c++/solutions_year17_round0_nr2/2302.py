// Problem_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text


#define MAX_LENGTH_OF_N		(18)
static char *CalculateMaxTidy(char _N[]);

void main() {
	int _T; // , n, m;
	char _N[MAX_LENGTH_OF_N + 1];
	cin >> _T;  // read T. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= _T; ++i) {
		cin >> _N;  // read _N.
		cout << "Case #" << i << ": " << CalculateMaxTidy(_N) << endl;
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

static char *CalculateMaxTidy(char _N[])
{
	int len_of_N = strlen(_N);
	int start_of_break = 0;
	int was_break = 0;

	for (int i = 0; i < len_of_N - 1; i++)
	{
		if (_N[i] < _N[i + 1])
		{
			start_of_break = i + 1;
		} 
		else if (_N[i] > _N[i + 1])
		{
			was_break = 1;
			break;
		}
	}

	if (was_break)
	{
		_N[start_of_break] -= 1;
		for (int j = start_of_break + 1; j < len_of_N; j++)
		{
			_N[j] = '9';
		}

		if (_N[0] == '0')
		{
			_N++;
		}
	}

	return _N;
}
