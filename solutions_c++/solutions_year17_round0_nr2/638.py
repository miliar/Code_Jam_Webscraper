#include "StdAfx.h"
#include "TidyNumbers.h"

#include <iostream>
#include <string>
using namespace std;


TidyNumbers::TidyNumbers(void)
{
}


TidyNumbers::~TidyNumbers(void)
{
}



void TidyNumbers::Solve()
{
	long long t;
	cin >> t;

	for (long i = 0;i<t;i++)
	{
		long long N;
		cin >> N;

		long long g = N;
		long last = 9;
		long pr = -1;
		long cnt = 0;

		long arr[20];
		for (long f = 0;f<20;f++)
		{
			arr[f] = 0;
		}
		while (g>0)
		{
			cnt++;
			long curr = g%10;
			g = g / 10;
			if (curr <= last)
			{
				// no problem
				//B += exp * curr;
				last = curr;
			}
			else
			{
				pr = cnt-1;
				last = curr-1;
			}
			arr[cnt-1] = last;
		}


		long long exp = 1;
		long long B = 0;
		for (long j = 0;j< cnt;j++)
		{
			if ( j<pr)
			{
				B += exp * 9;
			}
			else
			{
				B += exp *arr[j];
			}
			exp *=10;
		}
		cout << "Case #" << (i+1) << ": " << B << std::endl; 

	}
}

