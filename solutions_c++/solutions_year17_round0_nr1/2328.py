// Problem_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text


//int main()
//{
//    return 0;
//}

#define MAX_LENGTH_OF_S		(1000)
static int CalculateFlips(char _S[], int _K);

void main() {
	int _T; // , n, m;
	char _S[MAX_LENGTH_OF_S + 1];
	int _K;
	int res;
	cin >> _T;  // read T. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= _T; ++i) {
		cin >> _S >> _K;  // read _S and then _K.
		cout << "Case #" << i << ": ";
		res = CalculateFlips(_S, _K);
		if(res == -1)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << res << endl;
		}
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

// return -1 if IMPOSSIBLE
static int CalculateFlips(char _S[], int _K)
{
	int flips = 0;
	int len_of_S = strlen(_S);
	for (int i = 0; i < len_of_S + 1 - _K; i++)
	{
		if (_S[i] == '-')
		{
			flips++;
			// make a flip of _K elements
			_S[i] = '+';
			for (int j = i + 1; j < i + _K; j++)
			{
				if (_S[j] == '-') 
				{
					_S[j] = '+';
				}
				else if (_S[j] == '+')
				{
					_S[j] = '-';
				}
			}
		}
		// otherwise ('+') - nothing to do
	}
	for (int z = 0; z < _K - 1; z++)
	{
		if (_S[len_of_S - z - 1] == '-')
		{
			flips = -1;
			break;
		}
	}
	return flips;
}

//typedef unsigned char	UINT8;
//typedef unsigned short	UINT16;
//typedef unsigned int	UINT32;
//#define TRUE		(1)
//#define FALSE		(0)
//
//#define MAX_UINT8			((UINT8)-1)
//
//#define MAX_NUM_FOR_S		(8)
//
//static UINT8 s_arrResults[MAX_NUM_FOR_S] = { MAX_UINT8, } ;
//
//#define GET_STEPS(_idx)				(s_arrResults[(_idx)])
//#define SET_STEPS(_idx, _steps)		s_arrResults[(_idx)] = (_steps)
//
//void CalculateTable(void)
//{
//	UINT8 idx = MAX_UINT8;
//	UINT8 bContinue = TRUE;
//
//	SET_STEPS(idx, 0);
//
//	while (bContinue)
//	{
//		UINT32 idx
//
//	}
//}
