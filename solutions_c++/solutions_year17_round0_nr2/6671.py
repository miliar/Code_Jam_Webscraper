// IOTutorial.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

/*
bool isTidy(long long N)
{
	bool isTidy = false;
	long long prevDig = -1;
	long long currDig = -1;
	if (N < 0)
		return true;

	prevDig = N % 10;
	N = N / 10;
	while (N > 0)
	{
		currDig = N % 10;
		if (currDig > prevDig)
			return false;
		prevDig = currDig;
		N = N / 10;
	}
	return true;
}

long long getLastTidy(long long N)
{
	while (N > 0)
	{
		if (isTidy(N))
			return N;
		N--;
	}
	//should not reach here
	return 1;
}
*/

long long getLastTidy(long long N)
{
	const int MAX = 19;// 10^18 is max
	long long digits[MAX];
	for (int i = 0; i < MAX; i++)
		digits[i] = 0;

	bool isTidy = false;
	long long prevDig = -1;
	long long currDig = -1;
	if (N < 10)
		return N;

	int idx = 0;
	prevDig = N % 10;
	digits[idx] = prevDig;
	N = N / 10;
	while (N > 0)
	{
		currDig = N % 10;
		if (currDig > prevDig)
		{
			// set all prevDig and former to 9
			int i = idx;
			while (i >= 0)
			{
				digits[i] = 9;
				--i;
			}
			// reduce currDig
			--currDig;
		}
		++idx;
		prevDig = currDig;
		digits[idx] = prevDig;
		N = N / 10;
	}

	// construct the number back
	long long retNum = 0;
	long long mult = 1;
	for (int i = 0; i <= idx; ++i)
	{
		retNum += digits[i] * mult;
		mult = mult * 10;
	}

	return retNum;
}

void main() {
	long long t, n;
	cin >> t;  // read t. cin knows that t is an long long, so it reads it as such.
	for (long long i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		cout << "Case #" << i << ": " << getLastTidy(n) << endl;
	}
}

