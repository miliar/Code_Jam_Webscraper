// 1ba.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//




#include "stdafx.h"


#include <iostream>
#include <fstream>
#include <algorithm>
# include <vector>
#include <string>
#include <queue>
#include <functional>

#define ffor(a,b,c) for(int (a)=(b);(a)<(c);(a)++)
#define INF 999999999

int main()
{

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	int NN; infile >> NN;

	ffor(iy, 1, NN + 1) {

		int N, R, O, Y, G, B, V;
		infile >> N;
		int col[6],nn[6];
		ffor(i, 0, 6) infile >> col[i];
		ffor(i, 0, 6)  col[i]=16*col[i]+i;
		std::sort(col, col + 6);
		ffor(i, 0, 6) { nn[i] = col[i] >> 4; col[i] = col[i] % 16; }
		iy = iy;
		std::string ans;
		std::string sel = "ROYGBV";
		if (nn[5] > (nn[4] + nn[3])) ans = "IMPOSSIBLE";
		else {
			
			ffor(i, 0, N) {
				if ((i % 2) == 0 && nn[5] != 0) {
					ans += sel[col[5]];
					nn[5]--;
				}
				else {
					if (nn[4] > nn[3]) { ans += sel[col[4]]; nn[4]--; }
					else {ans += sel[col[3]]; nn[3]--;}
				}

			}
		}


		
		


		//small cases

		
		
		outfile << "Case #" << iy << ": " <<ans  << std::endl;


	}

	return 0;
}

