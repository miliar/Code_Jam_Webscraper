// Tidy Numbers.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//



#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#define ffor(a,b,c) for(int (a)=(b);(a)<(c);(a)++)


int main()
{

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	int NN; infile >> NN;

	ffor(iy, 1, NN + 1) {
		__int64 N,N2; infile >> N;
		__int64 ans=0;

		int digit[20];
		int idx = 0;

		N2 = N;
		while (N2 > 0) {
			digit[idx] = int(N2 % 10);
			N2 = N2 / 10;
			idx++; //idx is the number of digits-1;
		}
		idx--;
		// find the first decreasing number
		int decre = idx+1;
		for (int i = idx; i > 0; i--) {
			if (digit[i] > digit[i - 1]) { decre = i; break; }
		}

		if (decre != idx+1) {
			// find the increasing number
			int incre = idx;
			for (int i = decre; i < idx; i++) {
				if (digit[i + 1] != digit[i])incre = i;

			}
			digit[incre]--;
			for (int i = incre - 1; i >= 0; i--) {
				digit[i] = 9;
			}
		}
		for (int i = idx; i >= 0; i--) ans = (ans * 10) + digit[i];

		outfile << "Case #" << iy << ": " << ans << std::endl;
	}

    return 0;
}

