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

		double D;int  N; infile >> D >> N;

		double K[1005], S[1005];
		ffor(i, 0, N) { infile >> K[i] >> S[i]; }
		
		double T2D[1005];
		ffor(i, 0, N)T2D[i] = (D - K[i]) / (S[i]);
		std::sort(T2D, T2D + N);
		double ans =D/ T2D[N - 1];



		//double dd = 0;
		//int mi = N, mj = N;
		//while (N > 1 && dd<=D) {
		//	double mtime = INF;
		//	ffor(i, 0, N) {
		//		ffor(j,0, N) {
		//			if (S[i]<S[j] && K[i]>K[j]) {
		//				double ftemp = ((S[j] - S[i]) / (K[i] - K[j]));
		//				if (mtime > ftemp) {
		//					mtime = ftemp; mi = i; mj = j;
		//				}
		//			}
		//				
		//		}
		//	}
		//}

		outfile.precision(15);

		outfile << "Case #" << iy << ": "  <<ans << std::endl;


	}

	return 0;
}

