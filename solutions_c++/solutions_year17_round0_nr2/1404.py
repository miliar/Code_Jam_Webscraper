#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;


long long gettidy(long long _N)
{
	long long NN = _N;
	int d = (int)log10((double)NN) + 1;
	long long r100 = (long long)pow((double)10, d - 1);
	for (; d > 1; d--)
	{
		long long digit1 = NN / r100;
		NN = NN % r100;
		r100 /= 10;
		long long digit2 = NN / r100;

		if(digit1 > digit2)
		{
			r100 *= 10;
			return (_N / r100) * r100 - 1;
		}
	}
	return _N;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		long long N;

		cin >> N;

		long long NN = -1;
		while(NN != N)
		{
			NN = N;
			N = gettidy(N);
		}

 		cout << "Case #" << numCase << ": ";
		cout << N;
 		cout << "\n";

		numCase++;
	}
	return 0;
}
