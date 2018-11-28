// BathroomStalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		int N, K;
		cin >> N >> K;

		int lg = static_cast<int>(log2(K)) + 1;
		int denominator = 1 << lg;// (int)pow(2, lg);
		int numerator1 = N - K;
		int numerator0 = numerator1 + denominator / 2;

 		int res0 = numerator0 / denominator;
 		int res1 = numerator1 / denominator;


		cout << "Case #" << t << ": "/* << N << " " << K << " "*/ << res0 << " " << res1 << endl;
	}

    return 0;
}

