// Bathroom Stalls.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#define ffor(a,b,c) for(int (a)=(b);(a)<(c);(a)++)


int main()
{

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	int NN; infile >> NN;

	ffor(iy, 1, NN + 1) {
		__int64 N, K;
		infile >> N >> K;

		__int64 lo = int( log2(K));

		__int64 K1 = int(pow(2, lo)) ;
		__int64 q, r;  

		q = (N-K1) /(K1); r = (N - K1 ) % K1;
		
		__int64 left, right;
		if (r >= K - K1) {
			q++;
		}
		if (q % 2 == 0) { left = q / 2-1; right = q / 2 ; }
		else { left = q / 2; right = q / 2; }



		outfile << "Case #" << iy << ": " << right<< " "<<left << std::endl;
	}

		return 0;
}

