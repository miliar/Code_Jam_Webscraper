// Problem_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define MAX_NUM_OF_N		(1000)
//#define PI					((double)(3.14159265358979))
//#define PI					((double)(3.141592653))
#define PI					((double)(3.14159265358979323846264338327950288419716939937510582097))
//#define PI					((double)(3.14159265358979))

static double CalcPancakes(int _N, int _K, int _R[], int _H[]);

void main() {
	int _T;
	int _N;
	int _K;
	int _R[MAX_NUM_OF_N];
	int _H[MAX_NUM_OF_N];
	double res;
	cin >> _T;  // read T. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= _T; ++i) {
		cin >> _N >> _K;  // read _N and then _K
		for (int j = 0; j < _N; j++)
		{
			cin >> _R[j] >> _H[j];
		}
		cout << "Case #" << i << ": ";
		res = CalcPancakes(_N, _K, _R, _H);
		printf("%.9f", res);
		cout << endl;
	}
}

static double CalcPancakes_3(int _N, int _K, int _R[], int _H[])
{
	double _S[MAX_NUM_OF_N];

	for (int i=0; i<_N; i++)
	{
		_S[i] = 2 * PI * _R[i] * _H[i];
	}

	// first sort
	for (int i = 0; i < _N - 1; i++)
	{
		for (int j = i + 1; j < _N; j++)
		{
			if (_S[i] < _S[j])
			{
				//swap
				double temp_S = _S[i];
				_S[i] = _S[j];
				_S[j] = temp_S;
			}
		}
	}

	double res = 0;
	for (int i = 0; i < _K; i++)
	{
		res += _S[i];
	}

	return res;
}

static double CalcPancakes_2(int _N, int _K, int _R[], int _H[])
{
	double max_res;
	if (_K == 1)
	{
		max_res = PI * _R[0] * _R[0] + 2 * PI * _R[0] * _H[0];

		for (int i = 1; i < _N; i++)
		{
			double res = PI * _R[i] * _R[i] + 2 * PI * _R[i] * _H[i];
			if (res > max_res)
			{
				max_res = res;
			}
		}
	}
	else // _K > 1
	{
		max_res = PI * _R[0] * _R[0] + 2 * PI * _R[0] * _H[0] + CalcPancakes_3(_N-1, _K-1, _R+1, _H+1);

		for (int i = 1; i <= _N - _K; i++)
		{
			double res = PI * _R[i] * _R[i] + 2 * PI * _R[i] * _H[i] + CalcPancakes_3(_N - 1 - i, _K - 1, _R + 1 + i, _H + 1 + i);
			if (res > max_res)
			{
				max_res = res;
			}
		}
	}

	return max_res;
}

static double CalcPancakes(int _N, int _K, int _R[], int _H[])
{
	// first sort
	for (int i = 0; i < _N-1; i++)
	{
		for (int j = i+1; j < _N; j++)
		{
			if ((_R[i] < _R[j]) || ((_R[i] == _R[j]) && (_H[i] < _H[j])))
			{
				//swap
				int temp_R = _R[i];
				_R[i] = _R[j];
				_R[j] = temp_R;
				int temp_H	= _H[i];
				_H[i] = _H[j];
				_H[j] = temp_H;
			}
		}
	}

	return CalcPancakes_2(_N, _K, _R, _H);
}
