// Oversized Pancake Flipper.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#define ffor(a,b,c) for(int (a)=(b);(a)<(c);(a)++)

#define MAX_N 2000

int dir[MAX_N];
int f[MAX_N];

int solve(int K, int N) {

	std::fill(f, f + N, 0);
	int ans = 0,sum = 0;
	for (int i = 0; i + K <= N; i++) {
		if ((dir[i] + sum) % 2 != 0) {ans++; f[i] = 1;}
		sum += f[i]; 
		if (i - K + 1 >= 0) sum -= f[i - K + 1];
	}
	for (int i = N - K + 1; i < N; i++) {
		if ((dir[i] + sum )% 2 != 0) return -1;
		if (i - K + 1 >= 0) sum -= f[i - K + 1];
	}
	return ans;
}

int main()
{

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	int NN; infile >> NN;


	ffor(iy, 1, NN + 1) {
		std::string S;
		infile >> S;
		int L = S.length();
		ffor(i, 0, L) {
			if (S[i] == '+') dir[i] = 0;
			else if (S[i] == '-')dir[i] = 1;
		}
		int K; infile >> K;
		int ans=solve(K,L);


		if(ans==-1)		outfile << "Case #" << iy << ": " << "IMPOSSIBLE"<< std::endl;
		else outfile << "Case #" << iy << ": " << ans << std::endl;
	}
    return 0;
}

