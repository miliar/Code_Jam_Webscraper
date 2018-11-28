// Problem_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define IS_ODD(_V)				(_V & 0x01)
static void CalculateDistance(long long _N, long long _K, long long &_D_MAX, long long &_D_MIN);

void main() {
	int _T;
	long long _N, _K, _D_MAX, _D_MIN;
	cin >> _T;  // read T. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= _T; ++i) {
		cin >> _N >> _K;  // read _N and then _K.
		cout << "Case #" << i << ": ";
		CalculateDistance(_N, _K, _D_MAX, _D_MIN);
		cout << _D_MAX << " " << _D_MIN << endl;
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

static void CalculateDistance(long long _N, long long _K, long long &_D_MAX, long long &_D_MIN)
{
	if (_K == 1)
	{
		if (IS_ODD(_N))
		{
			_D_MAX = _D_MIN = (_N / 2);
		}
		else
		{ 
			_D_MAX = (_N / 2);
			_D_MIN = _D_MAX - 1;
		}
	}
	else
	{
		if (IS_ODD(_N))
		{
			CalculateDistance(_N / 2, _K / 2, _D_MAX, _D_MIN);
		}
		else
		{
			if (IS_ODD(_K))
			{
				CalculateDistance((_N / 2) - 1, _K / 2, _D_MAX, _D_MIN);
			}
			else
			{
				CalculateDistance(_N / 2, _K / 2, _D_MAX, _D_MIN);
			}
		}
	}
}
